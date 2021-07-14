import uproot
import awkward as ak
import numpy as np
import glob
from numba import jit
#from tqdm import tqdm
import vector
import time

start_time = time.time()

# Using glob
dir_path = "/x4/cms/dylee/Delphes/data/Storage/Original_data/root/signal/Original/*.root"
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
	for arrays in uproot.iterate(flist,branches):
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

		# Muon Selection (Only used to calculate dR)
		Muon_mask = (Muon.PT > 15) & (np.abs(Muon.Eta) < 2.5) 
		Muon = Muon[Muon_mask]

		# Electron Selection
		Electron_mask = ((Electron.PT > 15) & (np.abs(Electron.Eta) < 1.442)) | ((Electron.PT > 15) & ((np.abs(Electron.Eta) > 1.566) & (np.abs(Electron.Eta < 2.5))))
		Electron = Electron[Electron_mask]

		# Apply lepton cuts
		Tri_electron_mask = ak.num(Electron) == 3

		Electron = Electron[Tri_electron_mask]
		Photon = Photon[Tri_electron_mask]
		MET = MET[Tri_electron_mask]
		Muon = Muon[Tri_electron_mask]
	
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

		eee_triplet_idx = find_3lep(Electron,ak.ArrayBuilder()).snapshot()
		ossf_mask = ak.num(eee_triplet_idx) == 2
		eee_triplet_idx = eee_triplet_idx[ossf_mask]
	
		eee_Electron = Electron[ossf_mask]
		eee_Photon = Photon[ossf_mask]
		eee_MET = MET[ossf_mask]

		print("---> Apply OSSF mask done : {0}".format(len(eee_Electron)))

		Triple_electron = [eee_Electron[eee_triplet_idx[idx]] for idx in "012"]

		
		# Define electron triplet
		Triple_eee = ak.zip({
			"lep1" : Triple_electron[0],
			"lep2" : Triple_electron[1],
			"lep3" : Triple_electron[2]
		})

		lepton1 = vector.obj(pt=Triple_eee.lep1.PT, phi=Triple_eee.lep1.Phi, eta=Triple_eee.lep1.Eta, mass=0)
		lepton2 = vector.obj(pt=Triple_eee.lep2.PT, phi=Triple_eee.lep2.Phi, eta=Triple_eee.lep2.Eta, mass=0)
		
		dilep = lepton1 + lepton2
		bestZ_idx = ak.singletons(ak.argmin(abs(dilep.mass - 91.1876), axis=1))
		
		Triple_eee = Triple_eee[bestZ_idx]
		
		print("---> Electron triplet define done : {0}".format(len(Triple_eee.lep1)))	

		
		## Event Selection

		# Electron PT cut
		Elept_mask = (Triple_eee.lep1.PT >= 25) & (Triple_eee.lep2.PT >= 15) & (Triple_eee.lep3.PT >= 25)
		Triple_eee = Triple_eee[Elept_mask]
		
		Elenum_mask = (ak.num(Triple_eee.lep1.PT) > 0) & (ak.num(Triple_eee.lep2.PT) > 0) & (ak.num(Triple_eee.lep3.PT) > 0)
		Triple_eee = Triple_eee[Elenum_mask]
		eee_Photon = eee_Photon[Elenum_mask]
		eee_MET = eee_MET[Elenum_mask]

		print("---> Electron PT cut done : {0}".format(len(Triple_eee.lep1)))	
	

		# MET cut
		MET_mask = (eee_MET.MET > 40)
		eee_MET = eee_MET[MET_mask]
		One_MET_mask = ak.num(eee_MET.MET) > 0

		Triple_eee = Triple_eee[One_MET_mask]
		eee_Photon = eee_Photon[One_MET_mask]		
		eee_MET = eee_MET[One_MET_mask]		

		print("---> MET selection done : {0}".format(len(Triple_eee.lep1)))


		# Z mass window 
		leading_electron = vector.obj(pt=Triple_eee.lep1.PT, phi=Triple_eee.lep1.Phi, eta=Triple_eee.lep1.Eta, mass=0)
		subleading_electron = vector.obj(pt=Triple_eee.lep2.PT, phi=Triple_eee.lep2.Phi, eta=Triple_eee.lep2.Eta, mass=0)

		dilep = leading_electron + subleading_electron

		zmass_window = (np.abs(dilep.mass - 91.1876) < 10)
		
		Triple_eee = Triple_eee[zmass_window]
		eee_Photon = eee_Photon[zmass_window]
		eee_MET = eee_MET[zmass_window]

		print("---> Z mass window done : {0}".format(len(ak.flatten(Triple_eee.lep1))))

		
		## Output Variable Define
		lep3_vec = vector.obj(pt=Triple_eee.lep3.PT, phi=Triple_eee.lep3.Phi)
		MET_vec = vector.obj(pt=eee_MET.MET, phi=eee_MET.Phi)
		MT_e = np.sqrt(2*(Triple_eee.lep3.PT)*(eee_MET.MET)*(1-np.cos(np.abs(MET_vec.deltaphi(lep3_vec)))))	
		
		leading_electron = vector.obj(pt=Triple_eee.lep1.PT, phi=Triple_eee.lep1.Phi, eta=Triple_eee.lep1.Eta, mass=0)
		subleading_electron = vector.obj(pt=Triple_eee.lep2.PT, phi=Triple_eee.lep2.Phi, eta=Triple_eee.lep2.Eta, mass=0)
		
		third_electron = vector.obj(pt=Triple_eee.lep3.PT, phi=Triple_eee.lep3.Phi, eta=Triple_eee.lep3.Eta, mass=0)
		diele = leading_electron + subleading_electron

		
		# Flatten and Convert to numpy array
		diele_mass = ak.to_numpy(ak.flatten(diele.mass))
		MT = ak.to_numpy(ak.flatten(MT_e))
		
		lep1_pt = ak.to_numpy(ak.flatten(leading_electron.pt))
		lep1_eta = ak.to_numpy(ak.flatten(leading_electron.eta))
		lep1_phi = ak.to_numpy(ak.flatten(leading_electron.phi))
		lep1_F = ak.to_numpy(ak.flatten(Triple_eee.lep1.Charge * 1))		

		lep2_pt = ak.to_numpy(ak.flatten(subleading_electron.pt))
		lep2_eta = ak.to_numpy(ak.flatten(subleading_electron.eta))
		lep2_phi = ak.to_numpy(ak.flatten(subleading_electron.phi))
		lep2_F = ak.to_numpy(ak.flatten(Triple_eee.lep2.Charge * 1))	

		lep3_pt = ak.to_numpy(ak.flatten(third_electron.pt))
		lep3_eta = ak.to_numpy(ak.flatten(third_electron.eta))
		lep3_phi = ak.to_numpy(ak.flatten(third_electron.phi))
		lep3_F = ak.to_numpy(ak.flatten(Triple_eee.lep3.Charge * 1))

		pho_pt = ak.to_numpy(ak.flatten(eee_Photon.PT))
		pho_eta = ak.to_numpy(ak.flatten(eee_Photon.Eta))
		pho_phi = ak.to_numpy(ak.flatten(eee_Photon.Phi))

		MET_MET = ak.to_numpy(ak.flatten(eee_MET.MET))
		MET_phi = ak.to_numpy(ak.flatten(eee_MET.Phi))

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

			print("****** array size ****** : {0}".format(len(histo['lep1_pt'])))

	return histo

histo = Loop(file_list)

outname = dir_path.split("/")[-3]+"_"+dir_path.split("/")[-2]+"_eee.npy"
np.save(outname, histo, allow_pickle=True)

print("End Process.... MUYAHO!")
print("--- %s seconds ---" % (time.time() - start_time))



