import uproot
import awkward as ak
import numpy as np
import glob
from numba import jit
from tqdm import tqdm
import vector
import time

start_time = time.time()

# Using glob
dir_path = "/x6/spool/dylee/data/Storage/Tenth_data/root/ttbarG/Tenth/*.root"
file_list = glob.glob(dir_path)


# For uproot4
flist = []
for f in file_list:
	flist.append(f + ':Delphes')

print("---> Sample Files Read Done")

branches = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'PhotonLoose.PT', 'PhotonLoose.Eta', 'PhotonLoose.Phi', 'MuonLoose.PT', 'MuonLoose.Eta', 'MuonLoose.Phi', 'MuonLoose.Charge', 'PuppiMissingET.MET', 'PuppiMissingET.Phi']

#@jit 

def Loop(file_list):
	
	# Define Array
	histo = {}

	# Start File Loop
	for arrays in tqdm(uproot.iterate(flist,branches)):
		
		law_data = len(arrays)
		print("################## Number of event : {0}".format(law_data))

		Electron = ak.zip({
	
		"PT" : arrays[b"Electron.PT"],	
		"Eta" : arrays[b"Electron.Eta"],
		"Phi" : arrays[b"Electron.Phi"],
		"Charge" : arrays[b"Electron.Charge"]

		})

		Photon = ak.zip({

		"PT" : arrays[b"PhotonLoose.PT"],
		"Eta" : arrays[b"PhotonLoose.Eta"],
		"Phi" : arrays[b"PhotonLoose.Phi"],

		})

		Muon = ak.zip({

		"PT" : arrays[b"MuonLoose.PT"],
		"Eta" : arrays[b"MuonLoose.Eta"],
		"Phi" : arrays[b"MuonLoose.Phi"],
		"Charge" : arrays[b"MuonLoose.Charge"]
	
		})

		MET = ak.zip({

		"MET" : arrays[b"PuppiMissingET.MET"],
		"Phi" : arrays[b"PuppiMissingET.Phi"]

		})

		print("---> Variable define done : {0}".format(len(Muon)))

		## Lepton Selection

		# Muon Selection 
		Muon_mask = (Muon.PT > 15) & (np.abs(Muon.Eta) < 2.5) 
		PI_Muon = Muon[Muon_mask]

		# Electron Selection (Only used to calculate dR)
		Electron_mask = ((Electron.PT > 15) & (np.abs(Electron.Eta) < 1.442)) | ((Electron.PT > 15) & ((np.abs(Electron.Eta) > 1.566) & (np.abs(Electron.Eta < 2.5))))
		PI_Electron = Electron[Electron_mask]

		# Apply lepton cuts
		Tri_muon_mask = ak.num(PI_Muon) == 3
		no_electron_mask = ak.num(PI_Electron) == 0

		lepsel_mask = Tri_muon_mask & no_electron_mask

		lepsel_Electron = PI_Electron[lepsel_mask]
		lepsel_Photon = Photon[lepsel_mask]
		lepsel_MET = MET[lepsel_mask]
		lepsel_Muon = PI_Muon[lepsel_mask]
	
		print("---> Applying lepton selection done : {0}".format(len(lepsel_Muon.PT)))
	
		## Photon Selection
		Photon_vari_mask = ((lepsel_Photon.PT > 20) & (np.abs(lepsel_Photon.Eta) < 1.442)) | ((lepsel_Photon.PT > 20) & ((np.abs(lepsel_Photon.Eta) > 1.566) & (np.abs(lepsel_Photon.Eta < 2.5))))

		# Photon dR
		ele_pair = ak.cartesian({"pho": lepsel_Photon, "ele": lepsel_Electron}, nested=True)
		mu_pair = ak.cartesian({"pho": lepsel_Photon, "mu": lepsel_Muon}, nested=True)

		dR1_pho = vector.obj(pt=ele_pair.pho.PT, phi=ele_pair.pho.Phi, eta=ele_pair.pho.Eta, mass=0)
		dR1_ele = vector.obj(pt=ele_pair.ele.PT, phi=ele_pair.ele.Phi, eta=ele_pair.ele.Eta, mass=0)

		dR2_pho = vector.obj(pt=mu_pair.pho.PT, phi=mu_pair.pho.Phi, eta=mu_pair.pho.Eta, mass=0)
		dR2_mu = vector.obj(pt=mu_pair.mu.PT, phi=mu_pair.mu.Phi, eta=mu_pair.mu.Eta, mass=0)

		dR_ele_mask = ak.all(dR1_pho.deltaR(dR1_ele) > 0.5, axis=-1)
		dR_mu_mask = ak.all(dR2_pho.deltaR(dR2_mu) > 0.5, axis=-1)

		Photon_mask = Photon_vari_mask & dR_ele_mask & dR_mu_mask
		phosel_Photon = lepsel_Photon[Photon_mask]
	
		# Apply photon cuts
		One_photon_mask = ak.num(phosel_Photon) > 0
	
		phosel_Electron = lepsel_Electron[One_photon_mask]
		phosel_Photon = lepsel_Photon[One_photon_mask]
		phosel_MET = lepsel_MET[One_photon_mask]
		phosel_Muon = lepsel_Muon[One_photon_mask]
		phosel_Photon = phosel_Photon[ak.argmax(phosel_Photon.PT, axis=1, keepdims=True)]

		print("---> Applying photon selection done : {0}".format(len(phosel_Muon.PT)))
	
		## OSSF
		def find_3lep(events_leptons, builder):
		
			for leptons in events_leptons:
				builder.begin_list()
				nlep = len(leptons)
			
				for i0 in range(nlep):
					for i1 in range(i0+1, nlep):
						if leptons[i0].Charge + leptons[i1].Charge != 0: continue;

						for i2 in range(nlep):
							if len({i0, i1, i2}) < 3: continue;
							builder.begin_tuple(3)
							builder.index(0).integer(i0)
							builder.index(1).integer(i1)
							builder.index(2).integer(i2)
							builder.end_tuple()
				builder.end_list()
			return builder	

		mmm_triplet_idx = find_3lep(phosel_Muon,ak.ArrayBuilder()).snapshot()
		ossf_mask = ak.num(mmm_triplet_idx) == 2
		mmm_triplet_idx = mmm_triplet_idx[ossf_mask]
	
		ossf_Muon = phosel_Muon[ossf_mask]
		ossf_Photon = phosel_Photon[ossf_mask]
		ossf_MET = phosel_MET[ossf_mask]

		print("---> Apply OSSF mask done : {0}".format(len(ossf_Muon.PT)))

		try:
			Triple_muon = [ossf_Muon[mmm_triplet_idx[idx]] for idx in "012"]

			
			# Define electron triplet
			Triple_mmm = ak.zip({
				"lep1" : Triple_muon[0],
				"lep2" : Triple_muon[1],
				"lep3" : Triple_muon[2]
			})

			lepton1 = vector.obj(pt=Triple_mmm.lep1.PT, phi=Triple_mmm.lep1.Phi, eta=Triple_mmm.lep1.Eta, mass=0)
			lepton2 = vector.obj(pt=Triple_mmm.lep2.PT, phi=Triple_mmm.lep2.Phi, eta=Triple_mmm.lep2.Eta, mass=0)
			
			dilep = lepton1 + lepton2
			bestZ_idx = ak.singletons(ak.argmin(abs(dilep.mass - 91.1876), axis=1))
			
			Triple_mmm = Triple_mmm[bestZ_idx]
			
			print("---> Muon triplet define done : {0}".format(len(Triple_mmm.lep1.PT)))	

			
			## Event Selection

			# Electron PT cut
			Mupt_mask = (Triple_mmm.lep1.PT >= 25) & (Triple_mmm.lep2.PT >= 15) & (Triple_mmm.lep3.PT >= 25)
			Triple_mmm = Triple_mmm[Mupt_mask]
			
			Munum_mask = (ak.num(Triple_mmm.lep1.PT) > 0) & (ak.num(Triple_mmm.lep2.PT) > 0) & (ak.num(Triple_mmm.lep3.PT) > 0)
			ptcut_Triple_mmm = Triple_mmm[Munum_mask]
			ptcut_Photon = ossf_Photon[Munum_mask]
			ptcut_MET = ossf_MET[Munum_mask]

			print("---> Muon PT cut done : {0}".format(len(ak.flatten(ptcut_Triple_mmm.lep1.PT))))	
		

			# MET cut
			MET_mask = (ptcut_MET.MET > 40)
			ptcut_MET = ptcut_MET[MET_mask]
			One_MET_mask = ak.num(ptcut_MET.MET) > 0

			METsel_Triple_mmm = ptcut_Triple_mmm[One_MET_mask]
			METsel_Photon = ptcut_Photon[One_MET_mask]		
			METsel_MET = ptcut_MET[One_MET_mask]		

			print("---> MET selection done : {0}".format(len(ak.flatten(METsel_Triple_mmm.lep1.PT))))


			# Z mass window 
			leading_muon = vector.obj(pt=METsel_Triple_mmm.lep1.PT, phi=METsel_Triple_mmm.lep1.Phi, eta=METsel_Triple_mmm.lep1.Eta, mass=0)
			subleading_muon = vector.obj(pt=METsel_Triple_mmm.lep2.PT, phi=METsel_Triple_mmm.lep2.Phi, eta=METsel_Triple_mmm.lep2.Eta, mass=0)

			dilep = leading_muon + subleading_muon

			zmass_window = (np.abs(dilep.mass - 91.1876) < 10)
			
			zmass_Triple_mmm = METsel_Triple_mmm[zmass_window]
			zmass_Photon = METsel_Photon[zmass_window]
			zmass_MET = METsel_MET[zmass_window]

			print("---> Z mass window done : {0}".format(len(ak.flatten(zmass_Triple_mmm.lep1.PT))))

			
			## Output Variable Define
			lep3_vec = vector.obj(pt=zmass_Triple_mmm.lep3.PT, phi=zmass_Triple_mmm.lep3.Phi)
			MET_vec = vector.obj(pt=zmass_MET.MET, phi=zmass_MET.Phi)
			MT_m = np.sqrt(2*(zmass_Triple_mmm.lep3.PT)*(zmass_MET.MET)*(1-np.cos(np.abs(MET_vec.deltaphi(lep3_vec)))))	
			
			leading_muon = vector.obj(pt=zmass_Triple_mmm.lep1.PT, phi=zmass_Triple_mmm.lep1.Phi, eta=zmass_Triple_mmm.lep1.Eta, mass=0)
			subleading_muon = vector.obj(pt=zmass_Triple_mmm.lep2.PT, phi=zmass_Triple_mmm.lep2.Phi, eta=zmass_Triple_mmm.lep2.Eta, mass=0)
			
			third_muon = vector.obj(pt=zmass_Triple_mmm.lep3.PT, phi=zmass_Triple_mmm.lep3.Phi, eta=zmass_Triple_mmm.lep3.Eta, mass=0)
			diele = leading_muon + subleading_muon
			trilep = leading_muon + subleading_muon + third_muon
			
			# Flatten and Convert to numpy array
			diele_mass = ak.to_numpy(ak.flatten(diele.mass))
			MT = ak.to_numpy(ak.flatten(MT_m))
			
			lep1_pt = ak.to_numpy(ak.flatten(leading_muon.pt))
			lep1_eta = ak.to_numpy(ak.flatten(leading_muon.eta))
			lep1_phi = ak.to_numpy(ak.flatten(leading_muon.phi))
			lep1_F = ak.to_numpy(ak.flatten(zmass_Triple_mmm.lep1.Charge * 2))		

			lep2_pt = ak.to_numpy(ak.flatten(subleading_muon.pt))
			lep2_eta = ak.to_numpy(ak.flatten(subleading_muon.eta))
			lep2_phi = ak.to_numpy(ak.flatten(subleading_muon.phi))
			lep2_F = ak.to_numpy(ak.flatten(zmass_Triple_mmm.lep2.Charge * 2))	

			lep3_pt = ak.to_numpy(ak.flatten(third_muon.pt))
			lep3_eta = ak.to_numpy(ak.flatten(third_muon.eta))
			lep3_phi = ak.to_numpy(ak.flatten(third_muon.phi))
			lep3_F = ak.to_numpy(ak.flatten(zmass_Triple_mmm.lep3.Charge * 2))

			pho_pt = ak.to_numpy(ak.flatten(zmass_Photon.PT))
			pho_eta = ak.to_numpy(ak.flatten(zmass_Photon.Eta))
			pho_phi = ak.to_numpy(ak.flatten(zmass_Photon.Phi))

			MET_MET = ak.to_numpy(ak.flatten(zmass_MET.MET))
			MET_phi = ak.to_numpy(ak.flatten(zmass_MET.Phi))

			trilep_mass = ak.to_numpy(ak.flatten(trilep.mass))
			trilep_E = ak.to_numpy(ak.flatten(trilep.E))

			# Output hist & Ntuple
			if len(histo) == 0:
				histo['diele_mass'] = diele_mass
				histo['MT'] = MT
				histo['lep1_pt'] = lep1_pt
				histo['lep1_eta'] = lep1_eta
				histo['lep1_phi'] = lep1_phi
				histo['lep1_F'] = lep1_F
				histo['lep2_pt'] = lep2_pt
				histo['lep2_eta'] = lep2_eta
				histo['lep2_phi'] = lep2_phi
				histo['lep2_F'] = lep2_F
				histo['lep3_pt'] = lep3_pt
				histo['lep3_eta'] = lep3_eta
				histo['lep3_phi'] = lep3_phi
				histo['lep3_F'] = lep3_F
				histo['pho_pt']	= pho_pt
				histo['pho_eta'] = pho_eta
				histo['pho_phi'] = pho_phi
				histo['MET_MET'] = MET_MET
				histo['MET_phi'] = MET_phi
				histo['trilep_mass'] = trilep_mass
				histo['trilep_E'] = trilep_E
			
				histo['law'] = arrays
				histo['first'] = Muon
				histo['second'] = lepsel_Muon.PT
				histo['third'] = phosel_Muon.PT
				histo['fourth'] = ossf_Muon.PT
				histo['fifth'] = Triple_mmm.lep1.PT
				histo['sixth'] = ak.flatten(ptcut_Triple_mmm.lep1.PT)
				histo['seventh'] = ak.flatten(METsel_Triple_mmm.lep1.PT)
				histo['eighth'] = ak.flatten(zmass_Triple_mmm.lep1.PT)

			else:
				histo['diele_mass'] = np.concatenate([histo['diele_mass'], diele_mass])
				histo['MT'] = np.concatenate([histo['MT'], MT])
				histo['lep1_pt'] = np.concatenate([histo['lep1_pt'], lep1_pt])
				histo['lep1_eta'] = np.concatenate([histo['lep1_eta'], lep1_eta])
				histo['lep1_phi'] = np.concatenate([histo['lep1_phi'], lep1_phi])	
				histo['lep1_F'] = np.concatenate([histo['lep1_F'], lep1_F])
				histo['lep2_pt'] = np.concatenate([histo['lep2_pt'], lep2_pt])
				histo['lep2_eta'] = np.concatenate([histo['lep2_eta'], lep2_eta])
				histo['lep2_phi'] = np.concatenate([histo['lep2_phi'], lep2_phi])
				histo['lep2_F'] = np.concatenate([histo['lep2_F'], lep2_F])
				histo['lep3_pt'] = np.concatenate([histo['lep3_pt'], lep3_pt])
				histo['lep3_eta'] = np.concatenate([histo['lep3_eta'], lep3_eta])
				histo['lep3_phi'] = np.concatenate([histo['lep3_phi'], lep3_phi])
				histo['lep3_F'] = np.concatenate([histo['lep3_F'], lep3_F])
				histo['pho_pt'] = np.concatenate([histo['pho_pt'], pho_pt])
				histo['pho_eta'] = np.concatenate([histo['pho_eta'], pho_eta])
				histo['pho_phi'] = np.concatenate([histo['pho_phi'], pho_phi])
				histo['MET_MET'] = np.concatenate([histo['MET_MET'], MET_MET])
				histo['MET_phi'] = np.concatenate([histo['MET_phi'], MET_phi])
				histo['trilep_mass'] = np.concatenate([histo['trilep_mass'], trilep_mass])
				histo['trilep_E'] = np.concatenate([histo['trilep_E'], trilep_E])

				histo['law'] = np.concatenate([histo['law'], arrays])
				histo['first'] = np.concatenate([histo['first'], Muon])
				histo['second'] = np.concatenate([histo['second'], lepsel_Muon.PT])
				histo['third'] = np.concatenate([histo['third'], phosel_Muon.PT])
				histo['fourth'] = np.concatenate([histo['fourth'], ossf_Muon.PT])
				histo['fifth'] = np.concatenate([histo['fifth'], Triple_mmm.lep1.PT])
				histo['sixth'] = np.concatenate([histo['sixth'], ak.flatten(ptcut_Triple_mmm.lep1.PT)])
				histo['seventh'] = np.concatenate([histo['seventh'], ak.flatten(METsel_Triple_mmm.lep1.PT)])
				histo['eighth'] = np.concatenate([histo['eighth'], ak.flatten(zmass_Triple_mmm.lep1.PT)])


				print("law data : {0}".format(len(histo['law'])))
				print("law particle : {0}".format(len(histo['first'])))
				print("lepton sel : {0}".format(len(histo['second'])))
				print("photon sel : {0}".format(len(histo['third'])))
				print("ossf : {0}".format(len(histo['fourth'])))
				print("triplet : {0}".format(len(histo['fifth'])))
				print("lepton pt cut : {0}".format(len(histo['sixth'])))
				print("MET cut : {0}".format(len(histo['seventh'])))
				print("z mass window : {0}".format(len(histo['eighth'])))
				print("****** array size ****** : {0}".format(len(histo['lep1_pt'])))
		except ValueError:
			print("empty")
	return histo

histo = Loop(file_list)

outname = dir_path.split("/")[-3]+"_"+dir_path.split("/")[-2]+"_mmm.npy"
np.save('/x6/spool/dylee/data/numpy/fixver/mmm/{0}'.format(outname), histo, allow_pickle=True)

print("End Process.... MUYAHO!")
print("--- %s seconds ---" % (time.time() - start_time))



