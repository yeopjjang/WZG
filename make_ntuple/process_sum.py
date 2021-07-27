import awkward as ak
import numpy as np
import glob
from numba import jit
from tqdm import tqdm
import time

# Data path
signal = '/x6/spool/dylee/data/numpy/mmm/signal*.npy'
WG = '/x6/spool/dylee/data/numpy/mmm/WG*.npy'
ZG = '/x6/spool/dylee/data/numpy/mmm/ZG*.npy'
WW = '/x6/spool/dylee/data/numpy/mmm/WW*.npy'
WZ = '/x6/spool/dylee/data/numpy/mmm/WZ*.npy'
ZZ = '/x6/spool/dylee/data/numpy/mmm/ZZ*.npy'
WWW = '/x6/spool/dylee/data/numpy/mmm/WWW*.npy'
WWZ = '/x6/spool/dylee/data/numpy/mmm/WWZ*.npy'
WZZ = '/x6/spool/dylee/data/numpy/mmm/WZZ*.npy'
ZZZ = '/x6/spool/dylee/data/numpy/mmm/ZZZ*.npy'
ttbarG = '/x6/spool/dylee/data/numpy/mmm/ttbarG*.npy'

signal_proc_list = glob.glob(signal)
WG_proc_list = glob.glob(WG)
ZG_proc_list = glob.glob(ZG)
WW_proc_list = glob.glob(WW)
WZ_proc_list = glob.glob(WZ)
ZZ_proc_list = glob.glob(ZZ)
WWW_proc_list = glob.glob(WWW)
WWZ_proc_list = glob.glob(WWZ)
WZZ_proc_list = glob.glob(WZZ)
ZZZ_proc_list = glob.glob(ZZZ)
ttbarG_proc_list = glob.glob(ttbarG)


# Data load & Make array
def Load(proc_list):
	Original = np.load(proc_list[0],allow_pickle=True)[()]
	Second = np.load(proc_list[1],allow_pickle=True)[()]
	Third = np.load(proc_list[2],allow_pickle=True)[()]
	Fourth = np.load(proc_list[3],allow_pickle=True)[()]
	Fifth = np.load(proc_list[4],allow_pickle=True)[()]
	Sixth = np.load(proc_list[5],allow_pickle=True)[()]
	Seventh = np.load(proc_list[6],allow_pickle=True)[()]
	Eighth = np.load(proc_list[7],allow_pickle=True)[()]
	Nineth = np.load(proc_list[8],allow_pickle=True)[()]
	Tenth = np.load(proc_list[9],allow_pickle=True)[()]
	
	process_list = [Original, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Nineth, Tenth]	
	return process_list
		
signal_list = Load(signal_proc_list)
WG_list = Load(WG_proc_list)
ZG_list = Load(ZG_proc_list)
WW_list = Load(WW_proc_list)
WZ_list = Load(WZ_proc_list)
ZZ_list = Load(ZZ_proc_list)
WWW_list = Load(WWW_proc_list)
WWZ_list = Load(WWZ_proc_list)
WZZ_list = Load(WZZ_proc_list)
ZZZ_list = Load(ZZZ_proc_list)
ttbarG_list = Load(ttbarG_proc_list)


## Varable

def Loop(file_list):
	
	# Define Array
	histo={}

	# Start File Loop
	for arrays in file_list:
		try:		
			dilep_mass = arrays['diele_mass']
			MT = arrays['MT']
			trilep_mass = arrays['trilep_mass']
		#	trilep_E = arrays['trilep_E']
		
			lep1_pt = arrays['lep1_pt']
			lep1_eta = arrays['lep1_eta']
			lep1_phi = arrays['lep1_phi']
			lep1_F = arrays['lep1_F']
		
			lep2_pt = arrays['lep2_pt']	
			lep2_eta = arrays['lep2_eta']
			lep2_phi = arrays['lep2_phi']
			lep2_F = arrays['lep2_F']

			lep3_pt = arrays['lep3_pt']
			lep3_eta = arrays['lep3_eta']
			lep3_phi = arrays['lep3_phi']
			lep3_F = arrays['lep3_F']

			pho_pt = arrays['pho_pt']
			pho_eta = arrays['pho_eta']
			pho_phi = arrays['pho_phi']

			MET_MET = arrays['MET_MET']
			MET_phi = arrays['MET_phi']
				
	# Output hist & Ntuple
			if len(histo) == 0:
				histo['dilep_mass'] = dilep_mass
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
		#		histo['trilep_E'] = trilep_E

			else:
				histo['dilep_mass'] = np.concatenate([histo['dilep_mass'], dilep_mass])
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
		#		histo['trilep_E'] = np.concatenate(histo['trilep_E'], trilep_E)	
	
		except KeyError:
			print("empty") 

	return histo

WZG = Loop(signal_list)
WG = Loop(WG_list)
ZG = Loop(ZG_list)
WW = Loop(WW_list)
WZ = Loop(WZ_list)
ZZ = Loop(ZZ_list)
WWW = Loop(WWW_list)
WWZ = Loop(WWZ_list)
WZZ = Loop(WZZ_list)
ZZZ = Loop(ZZZ_list)
ttbarG = Loop(ttbarG_list)

print("Number of WZG event : {0}".format(len(WZG['dilep_mass'])))
print("Number of WG event : {0}".format(len(WG['dilep_mass'])))
print("Number of ZG event : {0}".format(len(ZG['dilep_mass'])))
print("Number of WW event : {0}".format(len(WW['dilep_mass'])))
print("Number of WZ event : {0}".format(len(WZ['dilep_mass'])))
print("Number of ZZ event : {0}".format(len(ZZ['dilep_mass'])))
print("Number of WWW event : {0}".format(len(WWW['dilep_mass'])))
print("Number of WWZ event : {0}".format(len(WWZ['dilep_mass'])))
print("Number of WZZ event : {0}".format(len(WZZ['dilep_mass'])))
print("Number of ZZZ event : {0}".format(len(ZZZ['dilep_mass'])))
print("Number of ttbarG event : {0}".format(len(ttbarG['dilep_mass'])))

mmm = {}
mmm['WZG'] = WZG
mmm['WG'] = WG
mmm['ZG'] = ZG
mmm['WW'] = WW
mmm['WZ'] = WZ
mmm['ZZ'] = ZZ
mmm['WWW'] = WWW
mmm['WWZ'] = WWZ
mmm['WZZ'] = WZZ
mmm['ZZZ'] = ZZZ
mmm['ttbarG'] = ttbarG

outname = "mmm_channel.npy"
np.save(outname, mmm)

print("MUYAHO!")













