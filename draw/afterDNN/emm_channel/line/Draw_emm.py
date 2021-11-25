import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

emm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/4096neuron/more/emm/prediction.csv'

emm_df = pd.read_csv(emm_infile)

emm_cut_df = emm_df[emm_df['prediction'] >= 0.98]

emm_idx = emm_cut_df.iloc[:,[0]].values.flatten()

emm_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/4096neuron/more/emm/emm_testset.h5'

emm_test_df = pd.read_hdf(emm_testset)

emm_after = emm_test_df.iloc[emm_idx]

emm_WZG = emm_after[emm_after['xsec'] == 0.00173]
emm_WG = emm_after[emm_after['xsec'] == 23.08]
emm_ZG = emm_after[emm_after['xsec'] == 4.977]
emm_WW = emm_after[emm_after['xsec'] == 3.356]
emm_WZ = emm_after[emm_after['xsec'] == 0.3983]
emm_ZZ = emm_after[emm_after['xsec'] == 0.04642]
emm_WWW = emm_after[emm_after['xsec'] == 0.001335]
emm_WWZ = emm_after[emm_after['xsec'] == 0.0003067]
emm_WZZ = emm_after[emm_after['xsec'] == 0.00002989]
emm_ZZZ = emm_after[emm_after['xsec'] == 0.000003157]
emm_ttbarG = emm_after[emm_after['xsec'] == 2.445]

# Plotting
lumi = 3000000

EventDict = {
"WZG" : 9899604/5,
"WG" : 10010000/5,
"ZG" : 10010000/5,
"WW" : 10010000/5,
"WZ" : 10010000/5,
"ZZ" : 10010000/5,
"WWW" : 10003323/5,
"WWZ" : 9995610/5,
"WZZ" : 10010000/5,
"ZZZ" : 10010000/5,
"ttbarG" : 10010000/5
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
WZG_Dilep_mass = emm_WZG['dilep_mass'].to_numpy()
WG_Dilep_mass = emm_WG['dilep_mass'].to_numpy()
ZG_Dilep_mass = emm_ZG['dilep_mass'].to_numpy()
WW_Dilep_mass = emm_WW['dilep_mass'].to_numpy()
WZ_Dilep_mass = emm_WZ['dilep_mass'].to_numpy()
ZZ_Dilep_mass = emm_ZZ['dilep_mass'].to_numpy()
WWW_Dilep_mass = emm_WWW['dilep_mass'].to_numpy()
WWZ_Dilep_mass = emm_WWZ['dilep_mass'].to_numpy()
WZZ_Dilep_mass = emm_WZZ['dilep_mass'].to_numpy()
ZZZ_Dilep_mass = emm_ZZZ['dilep_mass'].to_numpy()
ttbarG_Dilep_mass = emm_ttbarG['dilep_mass'].to_numpy()

# MT
WZG_MT = emm_WZG['MT'].to_numpy()
WG_MT = emm_WG['MT'].to_numpy()
ZG_MT = emm_ZG['MT'].to_numpy()
WW_MT = emm_WW['MT'].to_numpy()
WZ_MT = emm_WZ['MT'].to_numpy()
ZZ_MT = emm_ZZ['MT'].to_numpy()
WWW_MT = emm_WWW['MT'].to_numpy()
WWZ_MT = emm_WWZ['MT'].to_numpy()
WZZ_MT = emm_WZZ['MT'].to_numpy()
ZZZ_MT = emm_ZZZ['MT'].to_numpy()
ttbarG_MT = emm_ttbarG['MT'].to_numpy()

# Photon PT
WZG_pho = emm_WZG['pho_pt'].to_numpy()
WG_pho = emm_WG['pho_pt'].to_numpy()
ZG_pho = emm_ZG['pho_pt'].to_numpy()
WW_pho = emm_WW['pho_pt'].to_numpy()
WZ_pho = emm_WZ['pho_pt'].to_numpy()
ZZ_pho = emm_ZZ['pho_pt'].to_numpy()
WWW_pho = emm_WWW['pho_pt'].to_numpy()
WWZ_pho = emm_WWZ['pho_pt'].to_numpy()
WZZ_pho = emm_WZZ['pho_pt'].to_numpy()
ZZZ_pho = emm_ZZZ['pho_pt'].to_numpy()
ttbarG_pho = emm_ttbarG['pho_pt'].to_numpy()

# MET
WZG_MET = emm_WZG['MET_MET'].to_numpy()
WG_MET = emm_WG['MET_MET'].to_numpy()
ZG_MET = emm_ZG['MET_MET'].to_numpy()
WW_MET = emm_WW['MET_MET'].to_numpy()
WZ_MET = emm_WZ['MET_MET'].to_numpy()
ZZ_MET = emm_ZZ['MET_MET'].to_numpy()
WWW_MET = emm_WWW['MET_MET'].to_numpy()
WWZ_MET = emm_WWZ['MET_MET'].to_numpy()
WZZ_MET = emm_WZZ['MET_MET'].to_numpy()
ZZZ_MET = emm_ZZZ['MET_MET'].to_numpy()
ttbarG_MET = emm_ttbarG['MET_MET'].to_numpy()

# Trilep_mass
WZG_Trilep_mass = emm_WZG['trilep_mass'].to_numpy()
WG_Trilep_mass = emm_WG['trilep_mass'].to_numpy()
ZG_Trilep_mass = emm_ZG['trilep_mass'].to_numpy()
WW_Trilep_mass = emm_WW['trilep_mass'].to_numpy()
WZ_Trilep_mass = emm_WZ['trilep_mass'].to_numpy()
ZZ_Trilep_mass = emm_ZZ['trilep_mass'].to_numpy()
WWW_Trilep_mass = emm_WWW['trilep_mass'].to_numpy()
WWZ_Trilep_mass = emm_WWZ['trilep_mass'].to_numpy()
WZZ_Trilep_mass = emm_WZZ['trilep_mass'].to_numpy()
ZZZ_Trilep_mass = emm_ZZZ['trilep_mass'].to_numpy()
ttbarG_Trilep_mass = emm_ttbarG['trilep_mass'].to_numpy()

# Leading lepton pt
WZG_lep1_pt = emm_WZG['lep1_pt'].to_numpy()
WG_lep1_pt = emm_WG['lep1_pt'].to_numpy()
ZG_lep1_pt = emm_ZG['lep1_pt'].to_numpy()
WW_lep1_pt = emm_WW['lep1_pt'].to_numpy()
WZ_lep1_pt = emm_WZ['lep1_pt'].to_numpy()
ZZ_lep1_pt = emm_ZZ['lep1_pt'].to_numpy()
WWW_lep1_pt = emm_WWW['lep1_pt'].to_numpy()
WWZ_lep1_pt = emm_WWZ['lep1_pt'].to_numpy()
WZZ_lep1_pt = emm_WZZ['lep1_pt'].to_numpy()
ZZZ_lep1_pt = emm_ZZZ['lep1_pt'].to_numpy()
ttbarG_lep1_pt = emm_ttbarG['lep1_pt'].to_numpy()

# Subleading lepton pt
WZG_lep2_pt = emm_WZG['lep2_pt'].to_numpy()
WG_lep2_pt = emm_WG['lep2_pt'].to_numpy()
ZG_lep2_pt = emm_ZG['lep2_pt'].to_numpy()
WW_lep2_pt = emm_WW['lep2_pt'].to_numpy()
WZ_lep2_pt = emm_WZ['lep2_pt'].to_numpy()
ZZ_lep2_pt = emm_ZZ['lep2_pt'].to_numpy()
WWW_lep2_pt = emm_WWW['lep2_pt'].to_numpy()
WWZ_lep2_pt = emm_WWZ['lep2_pt'].to_numpy()
WZZ_lep2_pt = emm_WZZ['lep2_pt'].to_numpy()
ZZZ_lep2_pt = emm_ZZZ['lep2_pt'].to_numpy()
ttbarG_lep2_pt = emm_ttbarG['lep2_pt'].to_numpy()

# Third lepton pt
WZG_lep3_pt = emm_WZG['lep3_pt'].to_numpy()
WG_lep3_pt = emm_WG['lep3_pt'].to_numpy()
ZG_lep3_pt = emm_ZG['lep3_pt'].to_numpy()
WW_lep3_pt = emm_WW['lep3_pt'].to_numpy()
WZ_lep3_pt = emm_WZ['lep3_pt'].to_numpy()
ZZ_lep3_pt = emm_ZZ['lep3_pt'].to_numpy()
WWW_lep3_pt = emm_WWW['lep3_pt'].to_numpy()
WWZ_lep3_pt = emm_WWZ['lep3_pt'].to_numpy()
WZZ_lep3_pt = emm_WZZ['lep3_pt'].to_numpy()
ZZZ_lep3_pt = emm_ZZZ['lep3_pt'].to_numpy()
ttbarG_lep3_pt = emm_ttbarG['lep3_pt'].to_numpy()

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

# Draw hist
stak_Z = [WG_Dilep_mass, ZZZ_Dilep_mass, WZZ_Dilep_mass, WWW_Dilep_mass, WWZ_Dilep_mass, WW_Dilep_mass, ZG_Dilep_mass, ZZ_Dilep_mass, ttbarG_Dilep_mass, WZ_Dilep_mass]

stak_MT = [np.clip(WG_MT,0,250,WG_MT), np.clip(ZZZ_MT,0,250,ZZZ_MT), np.clip(WZZ_MT,0,250,WZZ_MT), np.clip(WWW_MT,0,250,WWW_MT), np.clip(WWZ_MT,0,250,WWZ_MT) , np.clip(WW_MT,0,250,WW_MT), np.clip(ZG_MT,0,250,ZG_MT), np.clip(ZZ_MT,0,250,ZZ_MT), np.clip(ttbarG_MT,0,250,ttbarG_MT), np.clip(WZ_MT,0,250,WZ_MT)]

stak_pho = [np.clip(WG_pho,0,600,WG_pho), np.clip(ZZZ_pho,0,600,ZZZ_pho), np.clip(WZZ_pho,0,600,WZZ_pho), np.clip(WWW_pho,0,600,WWW_pho), np.clip(WWZ_pho,0,600,WWZ_pho) , np.clip(WW_pho,0,600,WW_pho), np.clip(ZG_pho,0,600,ZG_pho), np.clip(ZZ_pho,0,600,ZZ_pho), np.clip(ttbarG_pho,0,600,ttbarG_pho), np.clip(WZ_pho,0,600,WZ_pho)]

stak_MET = [np.clip(WG_MET,0,660,WG_MET), np.clip(ZZZ_MET,0,660,ZZZ_MET), np.clip(WZZ_MET,0,660,WZZ_MET), np.clip(WWW_MET,0,660,WWW_MET), np.clip(WWZ_MET,0,660,WWZ_MET) , np.clip(WW_MET,0,660,WW_MET), np.clip(ZG_MET,0,660,ZG_MET), np.clip(ZZ_MET,0,660,ZZ_MET), np.clip(ttbarG_MET,0,660,ttbarG_MET), np.clip(WZ_MET,0,660,WZ_MET)]

stak_triM = [np.clip(WG_Trilep_mass,0,1400,WG_Trilep_mass), np.clip(ZZZ_Trilep_mass,0,1400,ZZZ_Trilep_mass), np.clip(WZZ_Trilep_mass,0,1400,WZZ_Trilep_mass), np.clip(WWW_Trilep_mass,0,1400,WWW_Trilep_mass), np.clip(WWZ_Trilep_mass,0,1400,WWZ_Trilep_mass) , np.clip(WW_Trilep_mass,0,1400,WW_Trilep_mass), np.clip(ZG_Trilep_mass,0,1400,ZG_Trilep_mass), np.clip(ZZ_Trilep_mass,0,1400,ZZ_Trilep_mass), np.clip(ttbarG_Trilep_mass,0,1400,ttbarG_Trilep_mass), np.clip(WZ_Trilep_mass,0,1400,WZ_Trilep_mass)]

stak_lep1_pt = [np.clip(WG_lep1_pt,0,660,WG_lep1_pt), np.clip(ZZZ_lep1_pt,0,660,ZZZ_lep1_pt), np.clip(WZZ_lep1_pt,0,660,WZZ_lep1_pt), np.clip(WWW_lep1_pt,0,660,WWW_lep1_pt), np.clip(WWZ_lep1_pt,0,660,WWZ_lep1_pt) , np.clip(WW_lep1_pt,0,660,WW_lep1_pt), np.clip(ZG_lep1_pt,0,660,ZG_lep1_pt), np.clip(ZZ_lep1_pt,0,660,ZZ_lep1_pt), np.clip(ttbarG_lep1_pt,0,660,ttbarG_lep1_pt), np.clip(WZ_lep1_pt,0,660,WZ_lep1_pt)]

stak_lep2_pt = [np.clip(WG_lep2_pt,0,420,WG_lep2_pt), np.clip(ZZZ_lep2_pt,0,420,ZZZ_lep2_pt), np.clip(WZZ_lep2_pt,0,420,WZZ_lep2_pt), np.clip(WWW_lep2_pt,0,420,WWW_lep2_pt), np.clip(WWZ_lep2_pt,0,420,WWZ_lep2_pt) , np.clip(WW_lep2_pt,0,420,WW_lep2_pt), np.clip(ZG_lep2_pt,0,420,ZG_lep2_pt), np.clip(ZZ_lep2_pt,0,420,ZZ_lep2_pt), np.clip(ttbarG_lep2_pt,0,420,ttbarG_lep2_pt), np.clip(WZ_lep2_pt,0,420,WZ_lep2_pt)]

stak_lep3_pt = [np.clip(WG_lep3_pt,0,460,WG_lep3_pt), np.clip(ZZZ_lep3_pt,0,460,ZZZ_lep3_pt), np.clip(WZZ_lep3_pt,0,460,WZZ_lep3_pt), np.clip(WWW_lep3_pt,0,460,WWW_lep3_pt), np.clip(WWZ_lep3_pt,0,460,WWZ_lep3_pt) , np.clip(WW_lep3_pt,0,460,WW_lep3_pt), np.clip(ZG_lep3_pt,0,460,ZG_lep3_pt), np.clip(ZZ_lep3_pt,0,460,ZZ_lep3_pt), np.clip(ttbarG_lep3_pt,0,460,ttbarG_lep3_pt), np.clip(WZ_lep3_pt,0,460,WZ_lep3_pt)]

we = [scales["WG"], scales["ZZZ"], scales["WZZ"], scales["WWW"], scales["WWZ"], scales["WW"], scales["ZG"], scales["ZZ"], scales["ttbarG"], scales["WZ"]]
co = ['darkorange','indigo', 'violet', 'darkgreen', 'darkslategray', 'aqua', 'maroon', 'blue', 'yellow', 'dodgerblue']
la = ['W+$\gamma$', 'ZZZ', 'WZZ', 'WWW', 'WWZ', 'WW', 'Z+$\gamma$', 'ZZ', '$t\overline{t}+\gamma$', 'WZ']

# Z MASS
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, range=(81.1876, 101.1876), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_Z, range=(81.1876, 101.1876), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 90)
plt.text(82, 80, '(e$\mu\mu$ channel)', fontsize=20)
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
plt.hist(np.clip(WZG_MT,0,250,WZG_MT), range=(0, 250), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_MT, range=(0, 250), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 250)
plt.ylim(0, 70)
plt.text(20, 61, '(e$\mu\mu$ channel)', fontsize=20)
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
plt.hist(np.clip(WZG_pho,0,600,WZG_pho), range=(0, 600), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_pho, range=(0, 600), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 600)
plt.ylim(0.01, 1000)
plt.text(200, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Photon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 30 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_phopt")
plt.show()
plt.close()

# MET
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_MET,0,660,WZG_MET), range=(0, 660), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_MET, range=(0, 660), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 660)
plt.ylim(0.01, 1000)
plt.text(220, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$E_{T}^{miss}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 33 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_MET")
plt.show()
plt.close()

# Trilep Mass
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_Trilep_mass,0,1400,WZG_Trilep_mass), range=(0, 1400), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_triM, range=(0, 1400), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1400)
plt.ylim(0.01, 1000)
plt.text(500, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("$M_{e\mu\mu}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 70 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_Trilep_mass")
plt.show()
plt.close()

# Leading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep1_pt,0,660,WZG_lep1_pt), range=(0, 660), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep1_pt, range=(0, 660), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 660)
plt.ylim(0.01, 1000)
plt.text(220, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Leading Muon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 33 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep1_pt")
plt.show()
plt.close()

# Subleading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep2_pt,0,420,WZG_lep2_pt), range=(0, 420), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep2_pt, range=(0, 420), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 420)
plt.ylim(0.01, 1000)
plt.text(180, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Sub-leading Muon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 21 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep2_pt")
plt.show()
plt.close()

# Third lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.clip(WZG_lep3_pt,0,460,WZG_lep3_pt), range=(0, 460), bins=20, weights=scales["WZG"], color='red', histtype='step', label='WZ$\gamma$(signal)', linewidth=3)
plt.hist(stak_lep3_pt, range=(0, 460), alpha=0.7, weights=we, bins=20, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 460)
plt.ylim(0.01, 1000)
plt.text(200, 200, '(e$\mu\mu$ channel)', fontsize=20)
plt.xlabel("Third Electron $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 23 GeV",fontsize=20, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.yscale('log')
plt.savefig("emm_lep3_pt")
plt.show()
plt.close()

