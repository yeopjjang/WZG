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

print("---> Variable define done : {0}".format(len(Electron)))


## Lepton Selection eem

# Muon Selection
Muon_mask = (Muon.PT > 15) & (np.abs(Muon.Eta) < 2.5)
Muon = Muon[Muon_mask]

# Electron Selection
Electron_mask = ((Electron.PT > 15) & (np.abs(Electron.Eta) < 1.442)) | ((Electron.PT > 15) & ((np.abs(Electron.Eta) > 1.566) & (np.abs(Electron.Eta < 2.5))))
Electron = Electron[Electron_mask]


# Apply lepton cuts
Di_electron_mask = ak.num(Electron) == 2
Single_muon_mask = ak.num(Muon) == 1

Channel_mask = Di_electron_mask & Single_muon_mask

Electron = Electron[Channel_mask]
Photon = Photon[Channel_mask]
MET = MET[Channel_mask]
Muon = Muon[Channel_mask]

print("---> Applying lepton selection done : {0}".format(len(Electron)))


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

print("---> Apply photon selection done : {0}".format(len(Electron)))


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

ee_doublet_idx = find_2lep(Electron,ak.ArrayBuilder()).snapshot()
ossf_mask = ak.num(ee_doublet_idx) == 1
ee_doublet_idx = ee_doublet_idx[ossf_mask]

eem_Electron = Electron[ossf_mask]
eem_Photon = Photon[ossf_mask]
eem_MET = MET[ossf_mask]
eem_Muon = Muon[ossf_mask]

print("---> Apply OSSF Mask done : {0}".format(len(eem_Electron)))

Di_electron = [eem_Electron[ee_doublet_idx[idx]] for idx in "01"]


# Define electron doublet
Di_ele = ak.zip({
	"lep1" : Di_electron[0],
	"lep2" : Di_electron[1],
	"lep3" : eem_Muon
})	

lepton1 = make_TLV_lepton(Di_ele.lep1)
lepton2 = make_TLV_lepton(Di_ele.lep2)

diele = lepton1 + lepton2
diele_mass_ak0 = ak.from_awkward0(diele.mass)

bestZ_idx = ak.singletons(ak.argmin(abs(diele_mass_ak0 - 91.1876), axis=1))

Di_ele = Di_ele[bestZ_idx]

leading_electron = make_TLV_lepton(Di_ele.lep1)
subleading_electron = make_TLV_lepton(Di_ele.lep2)
third_muon = make_TLV_lepton(Di_ele.lep3)

leading_electron_charge = Di_ele.lep1.Charge
subleading_electron_charge = Di_ele.lep2.Charge
third_muon_charge = Di_ele.lep3.Charge

print("---> Electron doublet define done : {0}".format(len(Di_ele.lep1)))

eem_Photon = make_TLV_photon(eem_Photon)
eem_MET = make_TLV_MET(eem_MET)


## Event Selection

# Lepton PT cut
leppt_mask = (leading_electron.pt >= 25) & (subleading_electron.pt >= 15) & (third_muon.pt >= 25)

leading_electron = leading_electron[leppt_mask]
subleading_electron = subleading_electron[leppt_mask]
third_muon = third_muon[leppt_mask]
eem_Photon = eem_Photon[leppt_mask]
eem_MET = eem_MET[leppt_mask]

print("---> Lepton PT cut done : {0}".format(len(leading_electron)))


# MET
MET_mask = (eem_MET.pt > 40)
eem_MET = eem_MET[MET_mask]

One_MET_mask = ak.num(eem_MET.pt) > 0

leading_electron = leading_electron[One_MET_mask]
subleading_electron = subleading_electron[One_MET_mask]
third_muon = third_muon[One_MET_mask]
eem_Photon = eem_Photon[One_MET_mask]
eem_MET = eem_MET[One_MET_mask]

leading_electron_charge = leading_electron_charge[One_MET_mask]
subleading_electron_charge = subleading_electron_charge[One_MET_mask]
third_muon_charge = third_muon_charge[One_MET_mask]

print("---> MET selection done : {0}".format(len(leading_electron)))


# Z mass & MT
dilep = leading_electron + subleading_electron
trilep = leading_electron + subleading_electron + third_muon
trileppho = leading_electron + subleading_electron + third_muon + eem_Photon

lep3_T2Vec = TVector2Array.from_polar(third_muon.pt, third_muon.phi)

MET_T2Vec = TVector2Array.from_polar(eem_MET.pt, eem_MET.phi)

MT_m = np.sqrt(2*(third_muon.pt)*(eem_MET.pt)*(1-np.cos(np.abs(MET_T2Vec.delta_phi(lep3_T2Vec)))))

zmass_window = (np.abs(dilep.mass - 91.1876) < 10)

#MT_mask = (MT_m > 30)

leading_electron = leading_electron[zmass_window]
subleading_electron = subleading_electron[zmass_window]
third_muon = third_muon[zmass_window]

leading_electron_charge = leading_electron_charge[zmass_window]
subleading_electron_charge = subleading_electron_charge[zmass_window]
third_muon_charge = third_muon_charge[zmass_window]

dilep = dilep[zmass_window]
trilep = trilep[zmass_window]
trileppho = trileppho[zmass_window]

MT_m = MT_m[zmass_window]
eem_MET = eem_MET[zmass_window]
eem_Photon = eem_Photon[zmass_window]

print("---> Z mass window done : {0}".format(len(dilep.mass.flatten())))

#Output hist & Ntuple
histo = {}

histo['Dilep'] = dilep
histo['Trilep'] = trilep
histo['Trileppho'] = trileppho
histo['lep1'] = leading_electron
histo['lep2'] = subleading_electron
histo['lep3'] = third_muon
histo['MET'] = eem_MET
histo['Pho'] = eem_Photon

histo['Dilep_PT'] = dilep.pt
histo['Dilep_Eta'] = dilep.eta
histo['Dilep_Phi'] = dilep.phi
histo['Dilep_mass'] = dilep.mass
histo['Dilep_E'] = dilep.E

histo['MT'] = MT_m
histo['absphi'] = np.abs(MET_T2Vec.delta_phi(lep3_T2Vec))
histo['Dilepptsum'] = leading_electron.pt + subleading_electron.pt
histo['Trilepptsum'] = leading_electron.pt + subleading_electron.pt + third_muon.pt
histo['Trilepphoptsum'] = leading_electron.pt + subleading_electron.pt + third_muon.pt + eem_Photon.pt

histo['lep1_PT'] = leading_electron.pt
histo['lep1_Eta'] = leading_electron.eta
histo['lep1_Phi'] = leading_electron.phi
histo['lep1_mass'] = leading_electron.mass
histo['lep1_E'] = leading_electron.E
histo['lep1_Flav'] = leading_electron.pt*0
histo['lep1_C'] = leading_electron_charge

histo['lep2_PT'] = subleading_electron.pt
histo['lep2_Eta'] = subleading_electron.eta
histo['lep2_Phi'] = subleading_electron.phi
histo['lep2_mass'] = subleading_electron.mass
histo['lep2_E'] = subleading_electron.E
histo['lep2_Flav'] = subleading_electron.pt*0
histo['lep2_C'] = subleading_electron_charge

histo['lep3_PT'] = third_muon.pt
histo['lep3_Eta'] = third_muon.eta
histo['lep3_Phi'] = third_muon.phi
histo['lep3_mass'] = third_muon.mass
histo['lep3_E'] = third_muon.E
histo['lep3_Flav'] = third_muon.pt*0+1
histo['lep3_C'] = third_muon_charge

histo['MET_PT'] = eem_MET.pt
histo['MET_Eta'] = eem_MET.eta
histo['MET_Phi'] = eem_MET.phi
histo['MET_E'] = eem_MET.E

histo['Pho_PT'] = eem_Photon.pt
histo['Pho_Eta'] = eem_Photon.eta
histo['Pho_Phi'] = eem_Photon.phi
histo['Pho_E'] = eem_Photon.E

outname = infile.split("/")[-3]+"_"+infile.split("/")[-2]+"_eem.npy"

np.save(outname, histo)

print("End process... MUYAHO!")

