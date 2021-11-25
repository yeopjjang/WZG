import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward1 as ak

# Data Load
infile = '/x4/cms/dylee/Delphes/analysis/ntuple/numpy/eee_channel.npy'

eee_channel = np.load(infile,allow_pickle=True)[()]

WZG = eee_channel['WZG']
WZG = eee_channel['WZG']
WG = eee_channel['WG']
ZG = eee_channel['ZG']
WW = eee_channel['WW']
WZ = eee_channel['WZ']
ZZ = eee_channel['ZZ']
WWW = eee_channel['WWW']
WWZ = eee_channel['WWZ']
WZZ = eee_channel['WZZ']
ZZZ = eee_channel['ZZZ']
ttbarG = eee_channel['ttbarG']

# Plotting
lumi = 3000000

EventDict = {
"WZG" : 9899604,
"WG" : 10010000,
"ZG" : 10010000,
"WW" : 10010000,
"WZ" : 10010000,
"ZZ" : 10010000,
"WWW" : 10003323,
"WWZ" : 9995610,
"WZZ" : 10010000,
"ZZZ" : 10010000,
"ttbarG" : 10010000
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

# Z mass
WZG_Dilep_mass = WZG['dilep_mass']
WG_Dilep_mass = WG['dilep_mass']
ZG_Dilep_mass = ZG['dilep_mass']
WW_Dilep_mass = WW['dilep_mass']
WZ_Dilep_mass = WZ['dilep_mass']
ZZ_Dilep_mass = ZZ['dilep_mass']
WWW_Dilep_mass = WWW['dilep_mass']
WWZ_Dilep_mass = WWZ['dilep_mass']
WZZ_Dilep_mass = WZZ['dilep_mass']
ZZZ_Dilep_mass = ZZZ['dilep_mass']
ttbarG_Dilep_mass = ttbarG['dilep_mass']

# MT 
WZG_MT = WZG['MT']
WG_MT = WG['MT']
ZG_MT = ZG['MT']
WW_MT = WW['MT']
WZ_MT = WZ['MT']
ZZ_MT = ZZ['MT']
WWW_MT = WWW['MT']
WWZ_MT = WWZ['MT']
WZZ_MT = WZZ['MT']
ZZZ_MT = ZZZ['MT']
ttbarG_MT = ttbarG['MT']

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, alpha=0.7, bins=300, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
#plt.ylim(0, 150)
plt.text(300, 10000, '(eee channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 10 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("sig_MT")
plt.show()
plt.close()


'''
# Photon PT
WZG_pho = WZG['pho_pt']
WG_pho = WG['pho_pt']
ZG_pho = ZG['pho_pt']
WW_pho = WW['pho_pt']
WZ_pho = WZ['pho_pt']
ZZ_pho = ZZ['pho_pt']
WWW_pho = WWW['pho_pt']
WWZ_pho = WWZ['pho_pt']
WZZ_pho = WZZ['pho_pt']
ZZZ_pho = ZZZ['pho_pt']
ttbarG_pho = ttbarG['pho_pt']

# MET
WZG_MET = WZG['MET_MET']
WG_MET = WG['MET_MET']
ZG_MET = ZG['MET_MET']
WW_MET = WW['MET_MET']
WZ_MET = WZ['MET_MET']
ZZ_MET = ZZ['MET_MET']
WWW_MET = WWW['MET_MET']
WWZ_MET = WWZ['MET_MET']
WZZ_MET = WZZ['MET_MET']
ZZZ_MET = ZZZ['MET_MET']
ttbarG_MET = ttbarG['MET_MET']

# Trilep_mass
WZG_Trilep_mass = WZG['trilep_mass']
WG_Trilep_mass = WG['trilep_mass']
ZG_Trilep_mass = ZG['trilep_mass']
WW_Trilep_mass = WW['trilep_mass']
WZ_Trilep_mass = WZ['trilep_mass']
ZZ_Trilep_mass = ZZ['trilep_mass']
WWW_Trilep_mass = WWW['trilep_mass']
WWZ_Trilep_mass = WWZ['trilep_mass']
WZZ_Trilep_mass = WZZ['trilep_mass']
ZZZ_Trilep_mass = ZZZ['trilep_mass']
ttbarG_Trilep_mass = ttbarG['trilep_mass']

# Trilep_E
WZG_Trilep_E = WZG['trilep_E']
WG_Trilep_E = WG['trilep_E']
ZG_Trilep_E = ZG['trilep_E']
WW_Trilep_E = WW['trilep_E']
WZ_Trilep_E = WZ['trilep_E']
ZZ_Trilep_E = ZZ['trilep_E']
WWW_Trilep_E = WWW['trilep_E']
WWZ_Trilep_E = WWZ['trilep_E']
WZZ_Trilep_E = WZZ['trilep_E']
ZZZ_Trilep_E = ZZZ['trilep_E']
ttbarG_Trilep_E = ttbarG['trilep_E']


# Number of events
print("WZG number of events : {0}".format(len(WZG_Dilep_mass)))
print("WG number of events : {0}".format(len(WG_Dilep_mass)))
print("ZG number of events : {0}".format(len(ZG_Dilep_mass)))
print("WW number of events : {0}".format(len(WW_Dilep_mass)))
print("WZ number of events : {0}".format(len(WZ_Dilep_mass)))
print("ZZ number of events : {0}".format(len(ZZ_Dilep_mass)))
print("WWW number of events : {0}".format(len(WWW_Dilep_mass)))
print("WWZ number of events : {0}".format(len(WWZ_Dilep_mass)))
print("WZZ number of events : {0}".format(len(WZZ_Dilep_mass)))
print("ZZZ number of events : {0}".format(len(ZZZ_Dilep_mass)))
print("ttbarG number of events : {0}".format(len(ttbarG_Dilep_mass)))

# Normalize
scales = {
        "WZG" : np.ones(len(WZG_Dilep_mass)) * lumi * xsecDict["WZG"] / EventDict['WZG'],
        "WG" : np.ones(len(WG_Dilep_mass)) * lumi * xsecDict["WG"] / EventDict['WG'],
        "ZG" : np.ones(len(ZG_Dilep_mass)) * lumi * xsecDict["ZG"] / EventDict['ZG'],
        "WW" : np.ones(len(WW_Dilep_mass)) * lumi * xsecDict["WW"] / EventDict['WW'],
        "WZ" : np.ones(len(WZ_Dilep_mass)) * lumi * xsecDict["WZ"] / EventDict['WZ'],
        "ZZ" : np.ones(len(ZZ_Dilep_mass)) * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
        "WWW" : np.ones(len(WWW_Dilep_mass)) * lumi * xsecDict["WWW"] / EventDict['WWW'],
        "WWZ" : np.ones(len(WWZ_Dilep_mass)) * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
        "WZZ" : np.ones(len(WZZ_Dilep_mass)) * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
        "ZZZ" : np.ones(len(ZZZ_Dilep_mass)) * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
        "ttbarG" : np.ones(len(ttbarG_Dilep_mass)) * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],
}

# Expected Yield
Yield = {

        "WZG" : len(WZG_Dilep_mass) * lumi * (xsecDict["WZG"] / EventDict['WZG']),
        "WG" : len(WG_Dilep_mass) * lumi * (xsecDict["WG"] / EventDict['WG']),
        "ZG" : len(ZG_Dilep_mass) * lumi * xsecDict["ZG"] / EventDict['ZG'],
        "WW" : len(WW_Dilep_mass) * lumi * xsecDict["WW"] / EventDict['WW'],
        "WZ" : len(WZ_Dilep_mass) * lumi * xsecDict["WZ"] / EventDict['WZ'],
        "ZZ" : len(ZZ_Dilep_mass) * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
        "WWW" : len(WWW_Dilep_mass) * lumi * xsecDict["WWW"] / EventDict['WWW'],
        "WWZ" : len(WWZ_Dilep_mass) * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
        "WZZ" : len(WZZ_Dilep_mass) * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
        "ZZZ" : len(ZZZ_Dilep_mass) * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
        "ttbarG" : len(ttbarG_Dilep_mass) * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],
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

print("Total bkg : {0}".format(total_bkg))

print("sf : {0}".format(Yield['WZG']/total_bkg))

sig = Yield['WZG']/np.sqrt(Yield['WZG']+total_bkg)

print("Significance : {0}".format(sig))

## Histogram Draw
stak_Z = [WG_Dilep_mass, ZZZ_Dilep_mass, WZZ_Dilep_mass, WWW_Dilep_mass, WWZ_Dilep_mass, WW_Dilep_mass, ZG_Dilep_mass, ZZ_Dilep_mass, ttbarG_Dilep_mass, WZ_Dilep_mass]

stak_MT = [WG_MT, ZZZ_MT, WZZ_MT, WWW_MT, WWZ_MT, WW_MT, ZG_MT, ZZ_MT, ttbarG_MT, WZ_MT]

stak_pho = [WG_pho, ZZZ_pho, WZZ_pho, WWW_pho, WWZ_pho, WW_pho, ZG_pho, ZZ_pho, ttbarG_pho, WZ_pho]

stak_MET= [WG_MET, ZZZ_MET, WZZ_MET, WWW_MET, WWZ_MET, WW_MET, ZG_MET, ZZ_MET, ttbarG_MET, WZ_MET]

stak_triM = [WG_Trilep_mass, ZZZ_Trilep_mass, WZZ_Trilep_mass, WWW_Trilep_mass, WWZ_Trilep_mass, WW_Trilep_mass, ZG_Trilep_mass, ZZ_Trilep_mass, ttbarG_Trilep_mass, WZ_Trilep_mass]

stak_triE = [WG_Trilep_E, ZZZ_Trilep_E, WZZ_Trilep_E, WWW_Trilep_E, WWZ_Trilep_E, WW_Trilep_E, ZG_Trilep_E, ZZ_Trilep_E, ttbarG_Trilep_E, WZ_Trilep_E]


we = [scales["WG"], scales["ZZZ"], scales["WZZ"], scales["WWW"], scales["WWZ"], scales["WW"], scales["ZG"], scales["ZZ"], scales["ttbarG"], scales["WZ"]]
co = ['darkorange','indigo', 'violet', 'darkgreen', 'darkslategray', 'dodgerblue', 'maroon', 'blue', 'yellow', 'aqua']
la = ['W+Gamma', 'ZZZ', 'WZZ', 'WWW', 'WWZ', 'WW', 'Z+Gamma', 'ZZ', 'ttbar+Gamma', 'WZ']


# Z MASS
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, range=(81.1876, 101.1876), bins=20, weights=scales["WZG"]*5, color='red', histtype='step', label='WZG(signalx5)', linewidth=3)
plt.hist(stak_Z, range=(81.1876, 101.1876), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 150)
plt.text(82, 130, '(eee channel)', fontsize=20)
plt.xlabel("M(ee) [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 1 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("eee_Dilep_mass")
plt.show()
plt.close()

# MT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, range=(0, 200), bins=20, weights=scales["WZG"]*5, color='red', histtype='step', label='WZG(signalx5)', linewidth=3)
plt.hist(stak_MT, range=(0, 200), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 200)
plt.ylim(0, 150)
plt.text(10, 135, '(eee channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 10 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("eee_MT")
plt.show()
plt.close()

# Photon PT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_pho, range=(0, 1500), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak_pho, range=(0, 1500), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1500)
plt.ylim(0.001, 10000)
plt.text(250, 2000, '(eee channel)', fontsize=20)
plt.xlabel("Photon $P_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 75 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("eee_phopt")
plt.show()
plt.close()

# MET
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MET, range=(0, 1500), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak_MET, range=(0, 1500), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1500)
plt.ylim(0.001, 10000)
plt.text(250, 2000, '(eee channel)', fontsize=20)
plt.xlabel("MET [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 75 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("eee_MET")
plt.show()
plt.close()

# Trilep Mass
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Trilep_mass, range=(0, 3000), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak_triM, range=(0, 3000), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 3000)
plt.ylim(0.001, 10000)
plt.text(1000, 2000, '(eee channel)', fontsize=20)
plt.xlabel("Tri-lepton Mass [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 150 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("eee_Trilep_mass")
plt.show()
plt.close()

# Trilep E
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Trilep_E, range=(0, 4000), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak_triE, range=(0, 4000), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 4000)
plt.ylim(0.001, 10000)
plt.text(1000, 2000, '(eee channel)', fontsize=20)
plt.xlabel("Tri-lepton Energy [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 200 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("eee_Trilep_E")
plt.show()
plt.close()
'''
