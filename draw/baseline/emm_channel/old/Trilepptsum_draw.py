import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward1 as ak

# Data load
Data = '/x4/cms/dylee/Delphes/analysis/ntuple/emm_channel.npy'

emm_channel = np.load(Data,allow_pickle=True)[()]

WZG = emm_channel['WZG']
WG = emm_channel['WG']
ZG = emm_channel['ZG']
WW = emm_channel['WW']
WZ = emm_channel['WZ']
ZZ = emm_channel['ZZ']
WWW = emm_channel['WWW']
WWZ = emm_channel['WWZ']
WZZ = emm_channel['WZZ']
ZZZ = emm_channel['ZZZ']
ttbarG = emm_channel['ttbarG']
'''
WZG_Pho_pt_mask = WZG.Pho_pt > 20
WG_Pho_pt_mask = WG.Pho_pt > 20
ZG_Pho_pt_mask = ZG.Pho_pt > 20
WW_Pho_pt_mask = WW.Pho_pt > 20
WZ_Pho_pt_mask = WZ.Pho_pt > 20
ZZ_Pho_pt_mask = ZZ.Pho_pt > 20
WWW_Pho_pt_mask = WWW.Pho_pt > 20
WWZ_Pho_pt_mask = WWZ.Pho_pt > 20
WZZ_Pho_pt_mask = WZZ.Pho_pt > 20
ZZZ_Pho_pt_mask = ZZZ.Pho_pt > 20
ttbarG_Pho_pt_mask = ttbarG.Pho_pt > 20

WZG = WZG[WZG_Pho_pt_mask]
WG = WG[WG_Pho_pt_mask]
ZG = ZG[ZG_Pho_pt_mask]
WW = WW[WW_Pho_pt_mask]
WZ = WZ[WZ_Pho_pt_mask]
ZZ = ZZ[ZZ_Pho_pt_mask]
WWW = WWW[WWW_Pho_pt_mask]
WWZ = WWZ[WWZ_Pho_pt_mask]
WZZ = WZZ[WZZ_Pho_pt_mask]
ZZZ = ZZZ[ZZZ_Pho_pt_mask]
ttbarG = ttbarG[ttbarG_Pho_pt_mask]
'''

# Plotting
lumi = 3000000

EventDict = {
"WZG" : 899604,
"WG" : 1010000,
"ZG" : 1010000,
"WW" : 1010000,
"WZ" : 1010000,
"ZZ" : 1010000,
"WWW" : 1003323,
"WWZ" : 995610,
"WZZ" : 1010000,
"ZZZ" : 1010000,
"ttbarG" : 1010000
}

xsecDict = {
"WZG" : 0.00173,
"WG" : 23.08,
"ZG" : 4.977,
"WW" : 3.356,
"WZ" : 0.3983,
"ZZ" : 0.04642,
"WWW" : 0.001335,
"WWZ" : 0.0003067,
"WZZ" : 0.00002989,
"ZZZ" : 0.000003157,
"ttbarG" : 2.445
}

'''
# Number of events
print("WZG number of events : {0}".format(len(WZG)))
print("WG number of events : {0}".format(len(WG)))
print("ZG number of events : {0}".format(len(ZG)))
print("WW number of events : {0}".format(len(WW)))
print("WZ number of events : {0}".format(len(WZ)))
print("ZZ number of events : {0}".format(len(ZZ)))
print("WWW number of events : {0}".format(len(WWW)))
print("WWZ number of events : {0}".format(len(WWZ)))
print("WZZ number of events : {0}".format(len(WZZ)))
print("ZZZ number of events : {0}".format(len(ZZZ)))
print("ttbarG number of events : {0}".format(len(ttbarG)))
'''

# Normalize
scales = {
	"WZG" : np.ones(len(WZG)) * lumi * xsecDict["WZG"] / EventDict['WZG'],
	"WG" : np.ones(len(WG)) * lumi * xsecDict["WG"] / EventDict['WG'],
       	"ZG" : np.ones(len(ZG)) * lumi * xsecDict["ZG"] / EventDict['ZG'],
        "WW" : np.ones(len(WW)) * lumi * xsecDict["WW"] / EventDict['WW'],
        "WZ" : np.ones(len(WZ)) * lumi * xsecDict["WZ"] / EventDict['WZ'],
        "ZZ" : np.ones(len(ZZ)) * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
        "WWW" : np.ones(len(WWW)) * lumi * xsecDict["WWW"] / EventDict['WWW'],
        "WWZ" : np.ones(len(WWZ)) * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
        "WZZ" : np.ones(len(WZZ)) * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
        "ZZZ" : np.ones(len(ZZZ)) * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
        "ttbarG" : np.ones(len(ttbarG)) * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

}


# Expected Yield
Yield = {

        "WZG" : len(WZG) * lumi * (xsecDict["WZG"] / EventDict['WZG']),
        "WG" : len(WG) * lumi * (xsecDict["WG"] / EventDict['WG']),
        "ZG" : len(ZG) * lumi * xsecDict["ZG"] / EventDict['ZG'],
        "WW" : len(WW) * lumi * xsecDict["WW"] / EventDict['WW'],
        "WZ" : len(WZ) * lumi * xsecDict["WZ"] / EventDict['WZ'],
        "ZZ" : len(ZZ) * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
        "WWW" : len(WWW) * lumi * xsecDict["WWW"] / EventDict['WWW'],
        "WWZ" : len(WWZ) * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
        "WZZ" : len(WZZ) * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
        "ZZZ" : len(ZZZ) * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
        "ttbarG" : len(ttbarG) * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

}

print("WZG expected yield : {0}".format(Yield['WZG']))
print("WG expected yield : {0}".format(Yield['WG']))
print("ZG expected yield : {0}".format(Yield['ZG']))
print("WW expected yield : {0}".format(Yield['WW']))
print("WZ expected yield : {0}".format(Yield['WZ']))
print("ZZ expected yield : {0}".format(Yield['ZZ']))
print("WWW expected yield : {0}".format(Yield['WWW']))
print("WWZ expected yield : {0}".format(Yield['WWZ']))
print("WZZ expected yield : {0}".format(Yield['WZZ']))
print("ZZZ expected yield : {0}".format(Yield['ZZZ']))
print("ttbarG expected yield : {0}".format(Yield['ttbarG']))


# Significance
total_bkg = (Yield['WG'] + Yield['ZG'] + Yield['WW'] + Yield['WZ'] + Yield['ZZ'] + Yield['WWW'] + Yield['WWZ'] + Yield['WZZ'] + Yield['ZZZ'] + Yield['ttbarG'])

print(total_bkg)

sig = Yield['WZG']/np.sqrt(total_bkg)

print("Significance : {0}".format(sig))

WZG_Trilepptsum = WZG.Trilepptsum
WG_Trilepptsum = WG.Trilepptsum
ZG_Trilepptsum = ZG.Trilepptsum
WW_Trilepptsum = WW.Trilepptsum
WZ_Trilepptsum = WZ.Trilepptsum
ZZ_Trilepptsum = ZZ.Trilepptsum
WWW_Trilepptsum = WWW.Trilepptsum
WWZ_Trilepptsum = WWZ.Trilepptsum
WZZ_Trilepptsum = WZZ.Trilepptsum
ZZZ_Trilepptsum = ZZZ.Trilepptsum
ttbarG_Trilepptsum = ttbarG.Trilepptsum

# Histogram Draw
stak = [ZZZ_Trilepptsum, WZZ_Trilepptsum, WWZ_Trilepptsum, WWW_Trilepptsum, ZZ_Trilepptsum, WZ_Trilepptsum, ttbarG_Trilepptsum, WW_Trilepptsum, ZG_Trilepptsum, WG_Trilepptsum]
we = [scales["ZZZ"], scales["WZZ"], scales["WWZ"], scales["WWW"], scales["ZZ"], scales["WZ"], scales["ttbarG"], scales["WW"], scales["ZG"], scales["WG"]]
co = ['r','r', 'r', 'r', 'dodgerblue', 'dodgerblue', 'lime', 'dodgerblue', 'indigo', 'indigo']
la = ['Tri-boson', '', '', '', 'Di-boson', '', 'ttbar+Gamma', '', 'V+Gamma', '']

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Trilepptsum, range=(0, 2000), bins=10, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak, range=(0, 2000), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 2000)
plt.ylim(0.001, 10000)
plt.text(20, 4000, '(emm channel)', fontsize=20)
plt.xlabel("Tri-lepton $p_{T}$ Sum [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 200 GeV",fontsize=15, loc='center')
plt.legend(fontsize=15, loc='upper right')
plt.yscale('log')
plt.savefig("emm_Trilepptsum")
plt.show()

