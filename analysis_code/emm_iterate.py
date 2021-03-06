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
dir_path = "/x6/spool/dylee/data/Storage/Original_data/root/signal/Original/*.root"
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
		print("################## Number of event : {0}".format(len(arrays)))

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

		print("---> Variable define done : {0}".format(len(Electron)))

		## Lepton Selection

		# Muon Selection
		Muon_mask = (Muon.PT > 15) & (np.abs(Muon.Eta) < 2.5) 
		Muon = Muon[Muon_mask]

		# Electron Selection
		Electron_mask = ((Electron.PT > 15) & (np.abs(Electron.Eta) < 1.442)) | ((Electron.PT > 15) & ((np.abs(Electron.Eta) > 1.566) & (np.abs(Electron.Eta < 2.5))))
		Electron = Electron[Electron_mask]

		# Apply lepton cuts
		Di_muon_mask = ak.num(Muon) == 2
		Single_electron_mask = ak.num(Electron) == 1

		Channel_mask = Di_muon_mask & Single_electron_mask

		Electron = Electron[Channel_mask]
		Photon = Photon[Channel_mask]
		MET = MET[Channel_mask]
		Muon = Muon[Channel_mask]
	
		print("---> Applying lepton selection done : {0}".format(len(Electron)))
	
		## Photon Selection
		Photon_vari_mask = ((Photon.PT > 20) & (np.abs(Photon.Eta) < 1.442)) | ((Photon.PT > 20) & ((np.abs(Photon.Eta) > 1.566) & (np.abs(Photon.Eta < 2.5))))

		# Photon dR
		ele_pair = ak.cartesian({"pho": Photon, "ele": Electron}, nested=True)
		mu_pair = ak.cartesian({"pho": Photon, "mu": Muon}, nested=True)

		dR1_pho = vector.obj(pt=ele_pair.pho.PT, phi=ele_pair.pho.Phi, eta=ele_pair.pho.Eta, mass=0)
		dR1_ele = vector.obj(pt=ele_pair.ele.PT, phi=ele_pair.ele.Phi, eta=ele_pair.ele.Eta, mass=0)

		dR2_pho = vector.obj(pt=mu_pair.pho.PT, phi=mu_pair.pho.Phi, eta=mu_pair.pho.Eta, mass=0)
		dR2_mu = vector.obj(pt=mu_pair.mu.PT, phi=mu_pair.mu.Phi, eta=mu_pair.mu.Eta, mass=0)

		dR_ele_mask = ak.all(dR1_pho.deltaR(dR1_ele) > 0.5, axis=-1)
		dR_mu_mask = ak.all(dR2_pho.deltaR(dR2_mu) > 0.5, axis=-1)

		Photon_mask = Photon_vari_mask & dR_ele_mask & dR_mu_mask
		Photon = Photon[Photon_mask]
	
		# Apply photon cuts
		One_photon_mask = ak.num(Photon) > 0
	
		Electron = Electron[One_photon_mask]
		Photon = Photon[One_photon_mask]
		MET = MET[One_photon_mask]
		Muon = Muon[One_photon_mask]
		Photon = Photon[ak.argmax(Photon.PT, axis=1, keepdims=True)]

		print("---> Applying photon selection done : {0}".format(len(Electron)))
	
		## OSSF
		def find_2lep(events_leptons, builder):
		
			for leptons in events_leptons:
				builder.begin_list()
				nlep = len(leptons)
			
				for i0 in range(nlep):
					for i1 in range(i0+1, nlep):
						if leptons[i0].Charge + leptons[i1].Charge != 0: continue;

						if nlep == 2:
							builder.begin_tuple(2)
							builder.index(0).integer(i0)
							builder.index(1).integer(i1)
							builder.end_tuple()

						else:
							for i2 in range(nlep):
								if len({i0, i1, i2}) < 3: continue;
								builder.begin_tuple(3)
								builder.index(0).integer(i0)
								builder.index(1).integer(i1)
								builder.index(2).integer(i2)
								builder.end_tuple()
				builder.end_list()
			return builder	

		mm_doublet_idx = find_2lep(Muon,ak.ArrayBuilder()).snapshot()
		ossf_mask = ak.num(mm_doublet_idx) == 1
		mm_doublet_idx = mm_doublet_idx[ossf_mask]
	
		emm_Electron = Electron[ossf_mask]
		emm_Photon = Photon[ossf_mask]
		emm_MET = MET[ossf_mask]
		emm_Muon = Muon[ossf_mask]

		print("---> Apply OSSF mask done : {0}".format(len(emm_Electron)))
	
		try:
			Di_muon = [emm_Muon[mm_doublet_idx[idx]] for idx in "01"]

			
			# Define electron triplet
			Di_mu = ak.zip({
				"lep1" : Di_muon[0],
				"lep2" : Di_muon[1],
				"lep3" : emm_Electron
			})

			lepton1 = vector.obj(pt=Di_mu.lep1.PT, phi=Di_mu.lep1.Phi, eta=Di_mu.lep1.Eta, mass=0)
			lepton2 = vector.obj(pt=Di_mu.lep2.PT, phi=Di_mu.lep2.Phi, eta=Di_mu.lep2.Eta, mass=0)
			
			dilep = lepton1 + lepton2
			bestZ_idx = ak.singletons(ak.argmin(abs(dilep.mass - 91.1876), axis=1))
			
			Di_mu = Di_mu[bestZ_idx]
			
			print("---> Muon doublet define done : {0}".format(len(Di_mu.lep1)))	

			
			## Event Selection

			# Electron PT cut
			leppt_mask = (Di_mu.lep1.PT >= 25) & (Di_mu.lep2.PT >= 15) & (Di_mu.lep3.PT >= 25)
			Di_mu = Di_mu[leppt_mask]
			
			lepnum_mask = (ak.num(Di_mu.lep1.PT) > 0) & (ak.num(Di_mu.lep2.PT) > 0) & (ak.num(Di_mu.lep3.PT) > 0)
			Di_mu = Di_mu[lepnum_mask]
			emm_Photon = emm_Photon[lepnum_mask]
			emm_MET = emm_MET[lepnum_mask]

			print("---> Lepton PT cut done : {0}".format(len(Di_mu.lep1)))	
		

			# MET cut
			MET_mask = (emm_MET.MET > 40)
			emm_MET = emm_MET[MET_mask]
			One_MET_mask = ak.num(emm_MET.MET) > 0

			Di_mu = Di_mu[One_MET_mask]
			emm_Photon = emm_Photon[One_MET_mask]		
			emm_MET = emm_MET[One_MET_mask]		

			print("---> MET selection done : {0}".format(len(Di_mu.lep1)))


			# Z mass window 
			leading_muon = vector.obj(pt=Di_mu.lep1.PT, phi=Di_mu.lep1.Phi, eta=Di_mu.lep1.Eta, mass=0)
			subleading_muon = vector.obj(pt=Di_mu.lep2.PT, phi=Di_mu.lep2.Phi, eta=Di_mu.lep2.Eta, mass=0)

			dilep = leading_muon + subleading_muon

			zmass_window = (np.abs(dilep.mass - 91.1876) < 10)
			
			Di_mu = Di_mu[zmass_window]
			emm_Photon = emm_Photon[zmass_window]
			emm_MET = emm_MET[zmass_window]

			print("---> Z mass window done : {0}".format(len(ak.flatten(Di_mu.lep1))))

			
			## Output Variable Define
			lep3_vec = vector.obj(pt=Di_mu.lep3.PT, phi=Di_mu.lep3.Phi)
			MET_vec = vector.obj(pt=emm_MET.MET, phi=emm_MET.Phi)
			MT_e = np.sqrt(2*(Di_mu.lep3.PT)*(emm_MET.MET)*(1-np.cos(np.abs(MET_vec.deltaphi(lep3_vec)))))	
			
			leading_muon = vector.obj(pt=Di_mu.lep1.PT, phi=Di_mu.lep1.Phi, eta=Di_mu.lep1.Eta, mass=0)
			subleading_muon = vector.obj(pt=Di_mu.lep2.PT, phi=Di_mu.lep2.Phi, eta=Di_mu.lep2.Eta, mass=0)	
			third_electron = vector.obj(pt=Di_mu.lep3.PT, phi=Di_mu.lep3.Phi, eta=Di_mu.lep3.Eta, mass=0)
			
			dimu = leading_muon + subleading_muon
			trilep = leading_muon + subleading_muon + third_electron
			
			# Flatten and Convert to numpy array
			dimu_mass = ak.to_numpy(ak.flatten(dimu.mass))
			MT = ak.to_numpy(ak.flatten(MT_e))
			
			lep1_pt = ak.to_numpy(ak.flatten(leading_muon.pt))
			lep1_eta = ak.to_numpy(ak.flatten(leading_muon.eta))
			lep1_phi = ak.to_numpy(ak.flatten(leading_muon.phi))
			lep1_F = ak.to_numpy(ak.flatten(Di_mu.lep1.Charge * 2))		

			lep2_pt = ak.to_numpy(ak.flatten(subleading_muon.pt))
			lep2_eta = ak.to_numpy(ak.flatten(subleading_muon.eta))
			lep2_phi = ak.to_numpy(ak.flatten(subleading_muon.phi))
			lep2_F = ak.to_numpy(ak.flatten(Di_mu.lep2.Charge * 2))	

			lep3_pt = ak.to_numpy(ak.flatten(third_electron.pt))
			lep3_eta = ak.to_numpy(ak.flatten(third_electron.eta))
			lep3_phi = ak.to_numpy(ak.flatten(third_electron.phi))
			lep3_F = ak.to_numpy(ak.flatten(Di_mu.lep3.Charge * 1))

			pho_pt = ak.to_numpy(ak.flatten(emm_Photon.PT))
			pho_eta = ak.to_numpy(ak.flatten(emm_Photon.Eta))
			pho_phi = ak.to_numpy(ak.flatten(emm_Photon.Phi))

			MET_MET = ak.to_numpy(ak.flatten(emm_MET.MET))
			MET_phi = ak.to_numpy(ak.flatten(emm_MET.Phi))

			trilep_mass = ak.to_numpy(ak.flatten(trilep.mass))
			trilep_E = ak.to_numpy(ak.flatten(trilep.E))

			# Output hist & Ntuple
			if len(histo) == 0:
				histo['dimu_mass'] = dimu_mass
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


			else:
				histo['dimu_mass'] = np.concatenate([histo['dimu_mass'], dimu_mass])
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

				print("****** array size ****** : {0}".format(len(histo['lep1_pt'])))
		except ValueError:
			print("empty")
	return histo

histo = Loop(file_list)

outname = dir_path.split("/")[-3]+"_"+dir_path.split("/")[-2]+"_emm.npy"
np.save('/x6/spool/dylee/data/numpy/emm/{0}'.format(outname), histo, allow_pickle=True)

print("End Process.... MUYAHO!")
print("--- %s seconds ---" % (time.time() - start_time))



