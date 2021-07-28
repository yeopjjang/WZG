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

print(total_bkg)

print("sf : {0}".format(Yield['WZG']/total_bkg))

sig = Yield['WZG']/np.sqrt(Yield['WZG']+total_bkg)

print("Significance : {0}".format(sig))


## Histogram Draw
stak_Z = [ZZZ_Dilep_mass, WZZ_Dilep_mass, WWZ_Dilep_mass, WWW_Dilep_mass, ZZ_Dilep_mass, WZ_Dilep_mass, WW_Dilep_mass, ttbarG_Dilep_mass, ZG_Dilep_mass, WG_Dilep_mass]

stak_MT = [ZZZ_MT, WZZ_MT, WWZ_MT, WWW_MT, ZZ_MT, WZ_MT, WW_MT, ttbarG_MT, ZG_MT, WG_MT]

stak_pho = [ZZZ_pho, WZZ_pho, WWZ_pho, WWW_pho, ZZ_pho, WZ_pho, WW_pho, ttbarG_pho, ZG_pho, WG_pho]

stak_MET= [ZZZ_MET, WZZ_MET, WWZ_MET, WWW_MET, ZZ_MET, WZ_MET, WW_MET, ttbarG_MET, ZG_MET, WG_MET]

we = [scales["ZZZ"], scales["WZZ"], scales["WWZ"], scales["WWW"], scales["ZZ"], scales["WZ"], scales["WW"], scales["ttbarG"], scales["ZG"], scales["WG"]]
co = ['indigo','violet', 'darkslategray', 'darkgreen', 'blue', 'aqua', 'dodgerblue', 'yellow', 'maroon', 'darkorange']
la = ['ZZZ', 'WZZ', 'WWZ', 'WWW', 'ZZ', 'WZ', 'WW', 'ttbar+Gamma', 'Z+Gamma', 'W+Gamma']


# Z MASS
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, range=(81.1876, 101.1876), bins=20, weights=scales["WZG"]*20, color='red', histtype='step', label='WZG(signalx20)', linewidth=3)
plt.hist(stak_Z, range=(81.1876, 101.1876), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 16000)
plt.text(82, 15000, '(eee channel)', fontsize=20)
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
plt.hist(WZG_MT, range=(0, 300), bins=20, weights=scales["WZG"]*20, color='red', histtype='step', label='WZG(signalx20)', linewidth=3)
plt.hist(stak_MT, range=(0, 300), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 300)
plt.ylim(0, 13000)
plt.text(50, 12000, '(eee channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 15 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("eee_MT")
plt.show()
plt.close()

# Photon PT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, range=(0, 1500), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZG(signal)', linewidth=3)
plt.hist(stak_pho, range=(0, 1500), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1500)
plt.ylim(0.0001, 10000000)
plt.text(250, 1000000, '(eee channel)', fontsize=20)
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
plt.hist(stak_pho, range=(0, 1500), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True,edgecolor='black', linewidth=0.5)
plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1500)
plt.ylim(0.0001, 1000000)
plt.text(250, 100000, '(eee channel)', fontsize=20)
plt.xlabel("MET [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 75 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("eee_MET")
plt.show()
plt.close()

















