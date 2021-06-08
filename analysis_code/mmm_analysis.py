import uproot3
import numpy as np
import awkward1 as ak
import matplotlib.pyplot as plt
import mplhep as hep
from uproot3_methods import TVector2Array, TLorentzVectorArray
import numba
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

Muon = ak.zip({

"PT" : tree["MuonLoose.PT"],
"Eta" : tree["MuonLoose.Eta"],
"Phi" : tree["MuonLoose.Phi"],
"Charge" : tree["MuonLoose.Charge"],
"T" : tree["MuonLoose.T"]

})

Electron = ak.zip({

"PT" : tree["Electron.PT"],
"Eta" : tree["Electron.Eta"],
"Phi" : tree["Electron.Phi"],
"Charge" : tree["Electron.Charge"],
"T" : tree["Electron.T"]

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

print("---> Variable define done : {0}".format(len(Muon)))


## Lepton Selection mmm

# Muon Selection
Muon_mask = (Muon.PT > 15) & (np.abs(Muon.Eta) < 2.5)
Muon = Muon[Muon_mask]

# Electron Selection(Only used to calculate dR)
Electron_mask = ((Electron.PT > 15) & (np.abs(Electron.Eta) < 1.442)) | ((Electron.PT > 15) & ((np.abs(Electron.Eta) > 1.566) & (np.abs(Electron.Eta < 2.5))))
Electron = Electron[Electron_mask]


# Apply lepton cuts
Tri_muon_mask = ak.num(Muon) == 3

Electron = Electron[Tri_muon_mask]
Photon = Photon[Tri_muon_mask]
MET = MET[Tri_muon_mask]
Muon = Muon[Tri_muon_mask]

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

Photon = Photon[ak.argmax(Photon.PT, axis=1, keepdims=True)]

print("---> Applying photon selection done : {0}".format(len(Muon)))


# OSSF
def find_3lep(events_leptons, builder):

	for leptons in events_leptons:
		builder.begin_list()
		nlep = len(leptons)
#		print("nlep : {0}".format(nlep))

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

mmm_triplet_idx = find_3lep(Muon,ak.ArrayBuilder()).snapshot()
ossf_mask = ak.num(mmm_triplet_idx) == 2
mmm_triplet_idx = mmm_triplet_idx[ossf_mask]

mmm_Muon = Muon[ossf_mask]
mmm_Photon = Photon[ossf_mask]
mmm_MET = MET[ossf_mask]

print("---> Apply OSSF Mask done : {0}".format(len(mmm_Muon)))

Triple_muon = [mmm_Muon[mmm_triplet_idx[idx]] for idx in "012"]


# Define muon triplet
Triple_mmm = ak.zip({
	"lep1" : Triple_muon[0],
	"lep2" : Triple_muon[1],
	"lep3" : Triple_muon[2]
})

lepton1 = make_TLV_lepton(Triple_mmm.lep1)
lepton2 = make_TLV_lepton(Triple_mmm.lep2)
lepton3 = make_TLV_lepton(Triple_mmm.lep3)

dimu = lepton1 + lepton2
dimu_mass_ak0 = ak.from_awkward0(dimu.mass)

bestZ_idx = ak.singletons(ak.argmin(abs(dimu_mass_ak0 - 91.1876), axis=1))

Triple_mmm = Triple_mmm[bestZ_idx]

leading_muon = make_TLV_lepton(Triple_mmm.lep1)
subleading_muon = make_TLV_lepton(Triple_mmm.lep2)
third_muon = make_TLV_lepton(Triple_mmm.lep3)

leading_muon_charge = Triple_mmm.lep1.Charge
subleading_muon_charge = Triple_mmm.lep2.Charge
third_muon_charge = Triple_mmm.lep3.Charge


print("---> Muon triplet define done : {0}".format(len(Triple_mmm.lep1)))

mmm_Photon = make_TLV_photon(mmm_Photon)
mmm_MET = make_TLV_MET(mmm_MET)


## Event Selection

# Muon PT cut
Mupt_mask = (leading_muon.pt >= 25) & (subleading_muon.pt >=15) & (third_muon.pt >= 25)

leading_muon = leading_muon[Mupt_mask]
subleading_muon = subleading_muon[Mupt_mask]
third_muon = third_muon[Mupt_mask]
mmm_Photon = mmm_Photon[Mupt_mask]
mmm_MET = mmm_MET[Mupt_mask]

print("---> Muon PT cut done : {0}".format(len(leading_muon)))


# MET
MET_mask = (mmm_MET.pt > 40)
mmm_MET = mmm_MET[MET_mask]

One_MET_mask = ak.num(mmm_MET.pt) > 0

leading_muon = leading_muon[One_MET_mask]
subleading_muon = subleading_muon[One_MET_mask]
third_muon = third_muon[One_MET_mask]
mmm_Photon = mmm_Photon[One_MET_mask]
mmm_MET = mmm_MET[One_MET_mask]

leading_muon_charge = leading_muon_charge[One_MET_mask]
subleading_muon_charge = subleading_muon_charge[One_MET_mask]
third_muon_charge = third_muon_charge[One_MET_mask]

print("---> MET selection done : {0}".format(len(leading_muon)))


# Z mass & MT
dilep = leading_muon + subleading_muon
trilep = leading_muon + subleading_muon + third_muon
trileppho = leading_muon + subleading_muon + third_muon + mmm_Photon

lep3_T2Vec = TVector2Array.from_polar(third_muon.pt, third_muon.phi)

MET_T2Vec = TVector2Array.from_polar(mmm_MET.pt, mmm_MET.phi)

MT_m = np.sqrt(2*(third_muon.pt)*(mmm_MET.pt)*(1-np.cos(np.abs(MET_T2Vec.delta_phi(lep3_T2Vec)))))

zmass_window = (np.abs(dilep.mass - 91.1876) < 10)

#MT_mask = (MT_m > 30)

leading_muon = leading_muon[zmass_window]
subleading_muon = subleading_muon[zmass_window]
third_muon = third_muon[zmass_window]

leading_muon_charge = leading_muon_charge[zmass_window]
subleading_muon_charge = subleading_muon_charge[zmass_window]
third_muon_charge = third_muon_charge[zmass_window]

dilep = dilep[zmass_window]
trilep = trilep[zmass_window]
trileppho = trileppho[zmass_window]

MT_m = MT_m[zmass_window]
mmm_MET = mmm_MET[zmass_window]
mmm_Photon = mmm_Photon[zmass_window]

print("---> Z mass window done : {0}".format(len(dilep.mass.flatten())))

# Output hist & Ntuple
histo = {}

histo['Dilep'] = dilep
histo['Trilep'] = trilep
histo['Trileppho'] = trileppho
histo['lep1'] = leading_muon
histo['lep2'] = subleading_muon
histo['lep3'] = third_muon
histo['MET'] = mmm_MET
histo['Pho'] = mmm_Photon

histo['Dilep_PT'] = dilep.pt
histo['Dilep_Eta'] = dilep.eta
histo['Dilep_Phi'] = dilep.phi
histo['Dilep_mass'] = dilep.mass
histo['Dilep_E'] = dilep.E

histo['MT'] = MT_m
histo['absphi'] = np.abs(MET_T2Vec.delta_phi(lep3_T2Vec))
histo['Dilepptsum'] = leading_muon.pt + subleading_muon.pt
histo['Trilepptsum'] = leading_muon.pt + subleading_muon.pt + third_muon.pt
histo['Trilepphoptsum'] = leading_muon.pt + subleading_muon.pt + third_muon.pt + mmm_Photon.pt

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

histo['lep3_PT'] = third_muon.pt
histo['lep3_Eta'] = third_muon.eta
histo['lep3_Phi'] = third_muon.phi
histo['lep3_mass'] = third_muon.mass
histo['lep3_E'] = third_muon.E
histo['lep3_Flav'] = third_muon.pt*0+1
histo['lep3_C'] = third_muon_charge

histo['MET_PT'] = mmm_MET.pt
histo['MET_Eta'] = mmm_MET.eta
histo['MET_Phi'] = mmm_MET.phi
histo['MET_E'] = mmm_MET.E

histo['Pho_PT'] = mmm_Photon.pt
histo['Pho_Eta'] = mmm_Photon.eta
histo['Pho_Phi'] = mmm_Photon.phi
histo['Pho_E'] = mmm_Photon.E

outname = infile.split("/")[-3]+"_"+infile.split("/")[-2]+"_mmm.npy"

np.save(outname, histo)

print("Process Done... MUYAHO!")
