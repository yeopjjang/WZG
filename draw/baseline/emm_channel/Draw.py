import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward1 as ak

# Data Load
infile = '/x4/cms/dylee/Delphes/analysis/ntuple/numpy/fixver/emm_channel.npy'

emm_channel = np.load(infile,allow_pickle=True)[()]

WZG = emm_channel['WZG']
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

# Leading lepton pt
WZG_lep1_pt = WZG['lep1_pt']
WG_lep1_pt = WG['lep1_pt']
ZG_lep1_pt = ZG['lep1_pt']
WW_lep1_pt = WW['lep1_pt']
WZ_lep1_pt = WZ['lep1_pt']
ZZ_lep1_pt = ZZ['lep1_pt']
WWW_lep1_pt = WWW['lep1_pt']
WWZ_lep1_pt = WWZ['lep1_pt']
WZZ_lep1_pt = WZZ['lep1_pt']
ZZZ_lep1_pt = ZZZ['lep1_pt']
ttbarG_lep1_pt = ttbarG['lep1_pt']

# Subleading lepton pt
WZG_lep2_pt = WZG['lep2_pt']
WG_lep2_pt = WG['lep2_pt']
ZG_lep2_pt = ZG['lep2_pt']
WW_lep2_pt = WW['lep2_pt']
WZ_lep2_pt = WZ['lep2_pt']
ZZ_lep2_pt = ZZ['lep2_pt']
WWW_lep2_pt = WWW['lep2_pt']
WWZ_lep2_pt = WWZ['lep2_pt']
WZZ_lep2_pt = WZZ['lep2_pt']
ZZZ_lep2_pt = ZZZ['lep2_pt']
ttbarG_lep2_pt = ttbarG['lep2_pt']

# Third lepton pt
WZG_lep3_pt = WZG['lep3_pt']
WG_lep3_pt = WG['lep3_pt']
ZG_lep3_pt = ZG['lep3_pt']
WW_lep3_pt = WW['lep3_pt']
WZ_lep3_pt = WZ['lep3_pt']
ZZ_lep3_pt = ZZ['lep3_pt']
WWW_lep3_pt = WWW['lep3_pt']
WWZ_lep3_pt = WWZ['lep3_pt']
WZZ_lep3_pt = WZZ['lep3_pt']
ZZZ_lep3_pt = ZZZ['lep3_pt']
ttbarG_lep3_pt = ttbarG['lep3_pt']

print(len(WZG['trilep_mass']))

'''
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

        "WZG" : len(WZG_Dilep_mass) * lumi * xsecDict["WZG"] / EventDict['WZG'],
        "WG" : len(WG_Dilep_mass) * lumi * xsecDict["WG"] / EventDict['WG'],
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

stak_MT = [np.clip(WG_MT,0,250,WG_MT), np.clip(ZZZ_MT,0,250,ZZZ_MT), np.clip(WZZ_MT,0,250,WZZ_MT), np.clip(WWW_MT,0,250,WWW_MT), np.clip(WWZ_MT,0,250,WWZ_MT) , np.clip(WW_MT,0,250,WW_MT), np.clip(ZG_MT,0,250,ZG_MT), np.clip(ZZ_MT,0,250,ZZ_MT), np.clip(ttbarG_MT,0,250,ttbarG_MT), np.clip(WZ_MT,0,250,WZ_MT)]

stak_pho = [np.clip(WG_pho,0,800,WG_pho), np.clip(ZZZ_pho,0,800,ZZZ_pho), np.clip(WZZ_pho,0,800,WZZ_pho), np.clip(WWW_pho,0,800,WWW_pho), np.clip(WWZ_pho,0,800,WWZ_pho) , np.clip(WW_pho,0,800,WW_pho), np.clip(ZG_pho,0,800,ZG_pho), np.clip(ZZ_pho,0,800,ZZ_pho), np.clip(ttbarG_pho,0,800,ttbarG_pho), np.clip(WZ_pho,0,800,WZ_pho)]

stak_MET = [np.clip(WG_MET,0,900,WG_MET), np.clip(ZZZ_MET,0,900,ZZZ_MET), np.clip(WZZ_MET,0,900,WZZ_MET), np.clip(WWW_MET,0,900,WWW_MET), np.clip(WWZ_MET,0,900,WWZ_MET) , np.clip(WW_MET,0,900,WW_MET), np.clip(ZG_MET,0,900,ZG_MET), np.clip(ZZ_MET,0,900,ZZ_MET), np.clip(ttbarG_MET,0,900,ttbarG_MET), np.clip(WZ_MET,0,900,WZ_MET)]

stak_triM = [np.clip(WG_Trilep_mass,0,1700,WG_Trilep_mass), np.clip(ZZZ_Trilep_mass,0,1700,ZZZ_Trilep_mass), np.clip(WZZ_Trilep_mass,0,1700,WZZ_Trilep_mass), np.clip(WWW_Trilep_mass,0,1700,WWW_Trilep_mass), np.clip(WWZ_Trilep_mass,0,1700,WWZ_Trilep_mass) , np.clip(WW_Trilep_mass,0,1700,WW_Trilep_mass), np.clip(ZG_Trilep_mass,0,1700,ZG_Trilep_mass), np.clip(ZZ_Trilep_mass,0,1700,ZZ_Trilep_mass), np.clip(ttbarG_Trilep_mass,0,1700,ttbarG_Trilep_mass), np.clip(WZ_Trilep_mass,0,1700,WZ_Trilep_mass)]

stak_lep1_pt = [np.clip(WG_lep1_pt,0,1000,WG_lep1_pt), np.clip(ZZZ_lep1_pt,0,1000,ZZZ_lep1_pt), np.clip(WZZ_lep1_pt,0,1000,WZZ_lep1_pt), np.clip(WWW_lep1_pt,0,1000,WWW_lep1_pt), np.clip(WWZ_lep1_pt,0,1000,WWZ_lep1_pt) , np.clip(WW_lep1_pt,0,1000,WW_lep1_pt), np.clip(ZG_lep1_pt,0,1000,ZG_lep1_pt), np.clip(ZZ_lep1_pt,0,1000,ZZ_lep1_pt), np.clip(ttbarG_lep1_pt,0,1000,ttbarG_lep1_pt), np.clip(WZ_lep1_pt,0,1000,WZ_lep1_pt)]

stak_lep2_pt = [np.clip(WG_lep2_pt,0,500,WG_lep2_pt), np.clip(ZZZ_lep2_pt,0,500,ZZZ_lep2_pt), np.clip(WZZ_lep2_pt,0,500,WZZ_lep2_pt), np.clip(WWW_lep2_pt,0,500,WWW_lep2_pt), np.clip(WWZ_lep2_pt,0,500,WWZ_lep2_pt) , np.clip(WW_lep2_pt,0,500,WW_lep2_pt), np.clip(ZG_lep2_pt,0,500,ZG_lep2_pt), np.clip(ZZ_lep2_pt,0,500,ZZ_lep2_pt), np.clip(ttbarG_lep2_pt,0,500,ttbarG_lep2_pt), np.clip(WZ_lep2_pt,0,500,WZ_lep2_pt)]

stak_lep3_pt = [np.clip(WG_lep3_pt,0,800,WG_lep3_pt), np.clip(ZZZ_lep3_pt,0,800,ZZZ_lep3_pt), np.clip(WZZ_lep3_pt,0,800,WZZ_lep3_pt), np.clip(WWW_lep3_pt,0,800,WWW_lep3_pt), np.clip(WWZ_lep3_pt,0,800,WWZ_lep3_pt) , np.clip(WW_lep3_pt,0,800,WW_lep3_pt), np.clip(ZG_lep3_pt,0,800,ZG_lep3_pt), np.clip(ZZ_lep3_pt,0,800,ZZ_lep3_pt), np.clip(ttbarG_lep3_pt,0,800,ttbarG_lep3_pt), np.clip(WZ_lep3_pt,0,800,WZ_lep3_pt)]

we = [scales["WG"], scales["ZZZ"], scales["WZZ"], scales["WWW"], scales["WWZ"], scales["WW"], scales["ZG"], scales["ZZ"], scales["ttbarG"], scales["WZ"]]
co = ['darkorange','indigo', 'violet', 'darkgreen', 'darkslategray', 'aqua', 'maroon', 'blue', 'yellow', 'dodgerblue']
la = ['W+$\gamma$', 'ZZZ', 'WZZ', 'WWW', 'WWZ', 'WW', 'Z+$\gamma$', 'ZZ', '$t\overline{t}+\gamma$', 'WZ']


# Z MASS
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, range=(81.1876, 101.1876), bins=20, weights=scales["WZG"]*5, color='red', histtype='step', label='WZ$\gamma$(signalx5)', linewidth=3)
plt.hist(stak_Z, range=(81.1876, 101.1876), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 300)
plt.text(82, 280, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$M_{\mu\mu}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 1 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("emm_Dilep_mass")
plt.show()
plt.close()

# MT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_MT,0,250,WZG_MT), range=(0, 250), bins=20, weights=scales["WZG"]*5, color='red', histtype='step', label='WZ$\gamma$(signalx5)', linewidth=3)
plt.hist(stak_MT, range=(0, 250), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 250)
plt.ylim(0, 300)
plt.text(20, 280, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 12.5 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("emm_MT")
plt.show()
plt.close()

# Photon PT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_pho,0,800,WZG_pho), range=(0, 800), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_pho, range=(0, 800), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 800)
plt.ylim(0.01, 10000)
plt.text(250, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Photon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 40 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_phopt")
plt.show()
plt.close()

# MET
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_MET,0,900,WZG_MET), range=(0, 900), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_MET, range=(0, 900), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 900)
plt.ylim(0.01, 10000)
plt.text(250, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$E_{T}^{miss}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 45 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_MET")
plt.show()
plt.close()

# Trilep Mass
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_Trilep_mass,0,1700,WZG_Trilep_mass), range=(0, 1700), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_triM, range=(0, 1700), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1700)
plt.ylim(0.01, 10000)
plt.text(500, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$M_{e\mu\mu}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 85 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_Trilep_mass")
plt.show()
plt.close()

# Leading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep1_pt,0,1000,WZG_lep1_pt), range=(0, 1000), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep1_pt, range=(0, 1000), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1000)
plt.ylim(0.01, 10000)
plt.text(300, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Leading Muon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 50 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep1_pt")
plt.show()
plt.close()

# Subleading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep2_pt,0,500,WZG_lep2_pt), range=(0, 500), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep2_pt, range=(0, 500), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0.01, 10000)
plt.text(200, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Sub-leading Muon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 25 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep2_pt")
plt.show()
plt.close()

# Third lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep3_pt,0,800,WZG_lep3_pt), range=(0, 800), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep3_pt, range=(0, 800), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 800)
plt.ylim(0.01, 10000)
plt.text(300, 2000, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Third Electron $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 40 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep3_pt")
plt.show()
plt.close()
'''
