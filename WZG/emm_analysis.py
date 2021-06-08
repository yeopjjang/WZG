import uproot3
import numpy as np
import awkward1 as ak
import matplotlib.pyplot as plt
import mplhep as hep
from uproot3_methods import TVector2Array, TLorentzVectorArray
import math
import sys

# Input files
infile = sys.argv[1]+"/*.root"
#infile = "/x4/cms/dylee/Delphes/data/root/signal/part1/DelPy_run_99_.root"
#infile = "/x4/cms/dylee/Delphes/data/root/signal/part1/*.root"


# Helper function
def make_TLV_photon(pho):
        pho = ak.to_awkward0(pho)
        TLV_photon = TLorentzVectorArray.from_ptetaphi(pho.PT, pho.Eta, pho.Phi, pho.T)
        return TLV_photon

def make_TLV_lepton(lep):
        lep = ak.to_awkward0(lep)
        TLV_lepton = TLorentzVectorArray.from_ptetaphim(lep.PT, lep.Eta, lep.Phi, lep.T)
        return TLV_lepton

def make_TLV_MET(MET):
        MET = ak.to_awkward0(MET)
        TLV_MET = TLorentzVectorArray.from_ptetaphim(MET.MET, MET.Eta, MET.Phi, MET.MET)
        return TLV_MET


# Output files name
sample_name = infile.split('/')[-1].split('.')[0]

print("---> Sample Files Read Done")


# Read tree
tree = uproot3.lazyarrays(
	infile,
	"Delphes",
	"*",
	entrysteps=1000,
)

Electron = ak.zip({

"PT" : tree["Electron.PT"],
"Eta" : tree["Electron.Eta"],
"Phi" : tree["Electron.Phi"],
"Charge" : tree["Electron.Charge"],
"T" : tree["Electron.T"]

})

Muon = ak.zip({

"PT" : tree["MuonLoose.PT"],
"Eta" : tree["MuonLoose.Eta"],
"Phi" : tree["MuonLoose.Phi"],
"Charge" : tree["MuonLoose.Charge"],
"T" : tree["MuonLoose.Charge"]

})

Photon = ak.zip({

"PT" : tree["PhotonLoose.PT"],
"Eta" : tree["PhotonLoose.Eta"],
"Phi" : tree["PhotonLoose.Phi"],
"T" : tree["PhotonLoose.T"]

})

MET = ak.zip({

"MET" : tree["PuppiMissingET.MET"], 
"Eta" : tree["PuppiMissingET.Eta"],
"Phi" : tree["PuppiMissingET.Phi"]

})

print("---> Variable define done")


## Lepton Selection emm

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

print("---> Applying lepton selection done : {0}".format(len(Muon)))


# Photon Selection
Photon_vari_mask = ((Photon.PT > 20) & (np.abs(Photon.Eta) < 1.442)) | ((Photon.PT > 20) & ((np.abs(Photon.Eta) > 1.566) & (np.abs(Photon.Eta < 2.5))))

# Photon dR
ele_pair = ak.cartesian({"pho": Photon, "ele": Electron}, nested=True)
mu_pair = ak.cartesian({"pho": Photon, "mu": Muon}, nested=True)

dR1_pho = make_TLV_photon(ele_pair.pho)
dR1_ele = make_TLV_lepton(ele_pair.ele)

dR2_pho = make_TLV_photon(mu_pair.pho)
dR2_mu = make_TLV_lepton(mu_pair.mu)

dR_ele_mask = ak.all(dR1_pho.delta_r(dR1_ele) > 0.5, axis=-1)
dR_mu_mask = ak.all(dR2_pho.delta_r(dR2_mu) > 0.5, axis=-1)

Photon_mask = Photon_vari_mask & dR_ele_mask & dR_mu_mask

Photon = Photon[Photon_mask]


# Apply photon cuts
One_photon_mask = ak.num(Photon) > 0

Electron = Electron[One_photon_mask]
Photon = Photon[One_photon_mask]
MET = MET[One_photon_mask]
Muon = Muon[One_photon_mask]

Photon= Photon[ak.argmax(Photon.PT, axis=1, keepdims=True)]

print("---> Apply photon selection done : {0}".format(len(Muon)))


## OSSF

def find_2lep(events_leptons,builder):
	for leptons in events_leptons:
		builder.begin_list()
		nlep = len(leptons)
		
		for i0 in range(nlep):
			for i1 in range(i0+1,nlep):
				if leptons[i0].Charge + leptons[i1].Charge != 0: continue;

				if nlep == 2:
					builder.begin_tuple(2)
					builder.index(0).integer(i0)
					builder.index(1).integer(i1)
					builder.end_tuple()

				else:
					for i2 in range(nlep):
						if len({i0,i1,i2}) < 3: continue;
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

print("---> Apply OSSF Mask done : {0}".format(len(emm_Muon)))

Di_muon = [emm_Muon[mm_doublet_idx[idx]] for idx in "01"]


# Define muon doublet
Di_mu = ak.zip({
	"lep1" : Di_muon[0],
	"lep2" : Di_muon[1],
	"lep3" : emm_Electron 
})	

lepton1 = make_TLV_lepton(Di_mu.lep1)
lepton2 = make_TLV_lepton(Di_mu.lep2)

dimu = lepton1 + lepton2
dimu_mass_ak0 = ak.from_awkward0(dimu.mass)

bestZ_idx = ak.singletons(ak.argmin(abs(dimu_mass_ak0 - 91.1876), axis=1))

Di_mu = Di_mu[bestZ_idx]

leading_muon = make_TLV_lepton(Di_mu.lep1)
subleading_muon = make_TLV_lepton(Di_mu.lep2)
third_electron = make_TLV_lepton(Di_mu.lep3)

leading_muon_charge = Di_mu.lep1.Charge
subleading_muon_charge = Di_mu.lep2.Charge
third_electron_charge = Di_mu.lep3.Charge

print("---> Muon doublet define done : {0}".format(len(Di_mu.lep1)))

emm_Photon = make_TLV_photon(emm_Photon)
emm_MET = make_TLV_MET(emm_MET)


## Event Selection

# Lepton PT cut
leppt_mask = (leading_muon.pt >= 25) & (subleading_muon.pt >= 15) & (third_electron.pt >= 25)

leading_muon = leading_muon[leppt_mask]
subleading_muon = subleading_muon[leppt_mask]
third_electron = third_electron[leppt_mask]
emm_Photon = emm_Photon[leppt_mask]
emm_MET = emm_MET[leppt_mask]

print("---> Lepton PT cut done : {0}".format(len(leading_muon)))


# MET
MET_mask = (emm_MET.pt > 40)
emm_MET = emm_MET[MET_mask]

One_MET_mask = ak.num(emm_MET.pt) > 0

leading_muon = leading_muon[One_MET_mask]
subleading_muon = subleading_muon[One_MET_mask]
third_electron = third_electron[One_MET_mask]
emm_Photon = emm_Photon[One_MET_mask]
emm_MET = emm_MET[One_MET_mask]

leading_muon_charge = leading_muon_charge[One_MET_mask]
subleading_muon_charge = subleading_muon_charge[One_MET_mask]
third_electron_charge = third_electron_charge[One_MET_mask]

print("---> MET selection done : {0}".format(len(leading_muon)))


# Z mass & MT
dilep = leading_muon + subleading_muon
trilep = leading_muon + subleading_muon + third_electron
trileppho = leading_muon + subleading_muon + third_electron + emm_Photon

lep3_T2Vec = TVector2Array.from_polar(third_electron.pt, third_electron.phi)

MET_T2Vec = TVector2Array.from_polar(emm_MET.pt, emm_MET.phi)

MT_e = np.sqrt(2*(third_electron.pt)*(emm_MET.pt)*(1-np.cos(np.abs(MET_T2Vec.delta_phi(lep3_T2Vec)))))

zmass_window = (np.abs(dilep.mass - 91.1876) < 10)

leading_muon = leading_muon[zmass_window]
subleading_muon = subleading_muon[zmass_window]
third_electron = third_electron[zmass_window]

leading_muon_charge = leading_muon_charge[zmass_window]
subleading_muon_charge = subleading_muon_charge[zmass_window]
third_electron_charge = third_electron_charge[zmass_window]

dilep = dilep[zmass_window]
trilep = trilep[zmass_window]
trileppho = trileppho[zmass_window]

MT_e = MT_e[zmass_window]
emm_MET = emm_MET[zmass_window]
emm_Photon = emm_Photon[zmass_window]

print("---> Z mass window done : {0}".format(len(dilep.mass.flatten())))


#Output hist & Ntuple

histo = {}

histo['Dilep'] = dilep
histo['Trilep'] = trilep
histo['Trileppho'] = trileppho
histo['lep1'] = leading_muon
histo['lep2'] = subleading_muon
histo['lep3'] = third_electron
histo['MET'] = emm_MET
histo['Pho'] = emm_Photon

histo['Dilep_PT'] = dilep.pt
histo['Dilep_Eta'] = dilep.eta
histo['Dilep_Phi'] = dilep.phi
histo['Dilep_mass'] = dilep.mass
histo['Dilep_E'] = dilep.E

histo['MT'] = MT_e
histo['absphi'] = np.abs(MET_T2Vec.delta_phi(lep3_T2Vec))
histo['Dilepptsum'] = leading_muon.pt + subleading_muon.pt
histo['Trilepptsum'] = leading_muon.pt + subleading_muon.pt + third_electron.pt
histo['Trilepphoptsum'] = leading_muon.pt + subleading_muon.pt + third_electron.pt + emm_Photon.pt

histo['lep1_PT'] = leading_muon.pt
histo['lep1_Eta'] = leading_muon.eta
histo['lep1_Phi'] = leading_muon.phi
histo['lep1_mass'] = leading_muon.mass
histo['lep1_E'] = leading_muon.E
histo['lep1_Flav'] = leading_muon.pt*0+1
histo['lep1_C'] = leading_muon_charge

histo['lep2_PT'] = subleading_muon.pt
histo['lep2_Eta'] = subleading_muon.eta
histo['lep2_Phi'] = subleading_muon.phi
histo['lep2_mass'] = subleading_muon.mass
histo['lep2_E'] = subleading_muon.E
histo['lep2_Flav'] = subleading_muon.pt*0+1
histo['lep2_C'] = subleading_muon_charge

histo['lep3_PT'] = third_electron.pt
histo['lep3_Eta'] = third_electron.eta
histo['lep3_Phi'] = third_electron.phi
histo['lep3_mass'] = third_electron.mass
histo['lep3_E'] = third_electron.E
histo['lep3_Flav'] = third_electron.pt*0
histo['lep3_C'] = third_electron_charge

histo['MET_PT'] = emm_MET.pt
histo['MET_Eta'] = emm_MET.eta
histo['MET_Phi'] = emm_MET.phi
histo['MET_E'] = emm_MET.E

histo['Pho_PT'] = emm_Photon.pt
histo['Pho_Eta'] = emm_Photon.eta
histo['Pho_Phi'] = emm_Photon.phi
histo['Pho_E'] = emm_Photon.E

outname = infile.split("/")[-3]+"_"+infile.split("/")[-2]+"_emm.npy"

np.save(outname, histo)

print("End process... MUYAHO!")

