import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

eem_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/more/eem/prediction.csv'

eem_df = pd.read_csv(eem_infile)

eem_cut_df = eem_df[eem_df['prediction'] >= 0.72]

eem_idx = eem_cut_df.iloc[:,[0]].values.flatten()

eem_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/more/eem/eem_testset.h5'

eem_test_df = pd.read_hdf(eem_testset)

eem_after = eem_test_df.iloc[eem_idx]

eem_WZG = eem_after[eem_after['xsec'] == 0.00173]
eem_WG = eem_after[eem_after['xsec'] == 23.08]
eem_ZG = eem_after[eem_after['xsec'] == 4.977]
eem_WW = eem_after[eem_after['xsec'] == 3.356]
eem_WZ = eem_after[eem_after['xsec'] == 0.3983]
eem_ZZ = eem_after[eem_after['xsec'] == 0.04642]
eem_WWW = eem_after[eem_after['xsec'] == 0.001335]
eem_WWZ = eem_after[eem_after['xsec'] == 0.0003067]
eem_WZZ = eem_after[eem_after['xsec'] == 0.00002989]
eem_ZZZ = eem_after[eem_after['xsec'] == 0.000003157]
eem_ttbarG = eem_after[eem_after['xsec'] == 2.445]

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
WZG_Dilep_mass = eem_WZG['dilep_mass'].to_numpy()
WG_Dilep_mass = eem_WG['dilep_mass'].to_numpy()
ZG_Dilep_mass = eem_ZG['dilep_mass'].to_numpy()
WW_Dilep_mass = eem_WW['dilep_mass'].to_numpy()
WZ_Dilep_mass = eem_WZ['dilep_mass'].to_numpy()
ZZ_Dilep_mass = eem_ZZ['dilep_mass'].to_numpy()
WWW_Dilep_mass = eem_WWW['dilep_mass'].to_numpy()
WWZ_Dilep_mass = eem_WWZ['dilep_mass'].to_numpy()
WZZ_Dilep_mass = eem_WZZ['dilep_mass'].to_numpy()
ZZZ_Dilep_mass = eem_ZZZ['dilep_mass'].to_numpy()
ttbarG_Dilep_mass = eem_ttbarG['dilep_mass'].to_numpy()

# MT
WZG_MT = eem_WZG['MT'].to_numpy()
WG_MT = eem_WG['MT'].to_numpy()
ZG_MT = eem_ZG['MT'].to_numpy()
WW_MT = eem_WW['MT'].to_numpy()
WZ_MT = eem_WZ['MT'].to_numpy()
ZZ_MT = eem_ZZ['MT'].to_numpy()
WWW_MT = eem_WWW['MT'].to_numpy()
WWZ_MT = eem_WWZ['MT'].to_numpy()
WZZ_MT = eem_WZZ['MT'].to_numpy()
ZZZ_MT = eem_ZZZ['MT'].to_numpy()
ttbarG_MT = eem_ttbarG['MT'].to_numpy()

# Photon PT
WZG_pho = eem_WZG['pho_pt'].to_numpy()
WG_pho = eem_WG['pho_pt'].to_numpy()
ZG_pho = eem_ZG['pho_pt'].to_numpy()
WW_pho = eem_WW['pho_pt'].to_numpy()
WZ_pho = eem_WZ['pho_pt'].to_numpy()
ZZ_pho = eem_ZZ['pho_pt'].to_numpy()
WWW_pho = eem_WWW['pho_pt'].to_numpy()
WWZ_pho = eem_WWZ['pho_pt'].to_numpy()
WZZ_pho = eem_WZZ['pho_pt'].to_numpy()
ZZZ_pho = eem_ZZZ['pho_pt'].to_numpy()
ttbarG_pho = eem_ttbarG['pho_pt'].to_numpy()

# MET
WZG_MET = eem_WZG['MET_MET'].to_numpy()
WG_MET = eem_WG['MET_MET'].to_numpy()
ZG_MET = eem_ZG['MET_MET'].to_numpy()
WW_MET = eem_WW['MET_MET'].to_numpy()
WZ_MET = eem_WZ['MET_MET'].to_numpy()
ZZ_MET = eem_ZZ['MET_MET'].to_numpy()
WWW_MET = eem_WWW['MET_MET'].to_numpy()
WWZ_MET = eem_WWZ['MET_MET'].to_numpy()
WZZ_MET = eem_WZZ['MET_MET'].to_numpy()
ZZZ_MET = eem_ZZZ['MET_MET'].to_numpy()
ttbarG_MET = eem_ttbarG['MET_MET'].to_numpy()

# Trilep_mass
WZG_Trilep_mass = eem_WZG['trilep_mass'].to_numpy()
WG_Trilep_mass = eem_WG['trilep_mass'].to_numpy()
ZG_Trilep_mass = eem_ZG['trilep_mass'].to_numpy()
WW_Trilep_mass = eem_WW['trilep_mass'].to_numpy()
WZ_Trilep_mass = eem_WZ['trilep_mass'].to_numpy()
ZZ_Trilep_mass = eem_ZZ['trilep_mass'].to_numpy()
WWW_Trilep_mass = eem_WWW['trilep_mass'].to_numpy()
WWZ_Trilep_mass = eem_WWZ['trilep_mass'].to_numpy()
WZZ_Trilep_mass = eem_WZZ['trilep_mass'].to_numpy()
ZZZ_Trilep_mass = eem_ZZZ['trilep_mass'].to_numpy()
ttbarG_Trilep_mass = eem_ttbarG['trilep_mass'].to_numpy()

# Leading lepton pt
WZG_lep1_pt = eem_WZG['lep1_pt'].to_numpy()
WG_lep1_pt = eem_WG['lep1_pt'].to_numpy()
ZG_lep1_pt = eem_ZG['lep1_pt'].to_numpy()
WW_lep1_pt = eem_WW['lep1_pt'].to_numpy()
WZ_lep1_pt = eem_WZ['lep1_pt'].to_numpy()
ZZ_lep1_pt = eem_ZZ['lep1_pt'].to_numpy()
WWW_lep1_pt = eem_WWW['lep1_pt'].to_numpy()
WWZ_lep1_pt = eem_WWZ['lep1_pt'].to_numpy()
WZZ_lep1_pt = eem_WZZ['lep1_pt'].to_numpy()
ZZZ_lep1_pt = eem_ZZZ['lep1_pt'].to_numpy()
ttbarG_lep1_pt = eem_ttbarG['lep1_pt'].to_numpy()

# Subleading lepton pt
WZG_lep2_pt = eem_WZG['lep2_pt'].to_numpy()
WG_lep2_pt = eem_WG['lep2_pt'].to_numpy()
ZG_lep2_pt = eem_ZG['lep2_pt'].to_numpy()
WW_lep2_pt = eem_WW['lep2_pt'].to_numpy()
WZ_lep2_pt = eem_WZ['lep2_pt'].to_numpy()
ZZ_lep2_pt = eem_ZZ['lep2_pt'].to_numpy()
WWW_lep2_pt = eem_WWW['lep2_pt'].to_numpy()
WWZ_lep2_pt = eem_WWZ['lep2_pt'].to_numpy()
WZZ_lep2_pt = eem_WZZ['lep2_pt'].to_numpy()
ZZZ_lep2_pt = eem_ZZZ['lep2_pt'].to_numpy()
ttbarG_lep2_pt = eem_ttbarG['lep2_pt'].to_numpy()

# Third lepton pt
WZG_lep3_pt = eem_WZG['lep3_pt'].to_numpy()
WG_lep3_pt = eem_WG['lep3_pt'].to_numpy()
ZG_lep3_pt = eem_ZG['lep3_pt'].to_numpy()
WW_lep3_pt = eem_WW['lep3_pt'].to_numpy()
WZ_lep3_pt = eem_WZ['lep3_pt'].to_numpy()
ZZ_lep3_pt = eem_ZZ['lep3_pt'].to_numpy()
WWW_lep3_pt = eem_WWW['lep3_pt'].to_numpy()
WWZ_lep3_pt = eem_WWZ['lep3_pt'].to_numpy()
WZZ_lep3_pt = eem_WZZ['lep3_pt'].to_numpy()
ZZZ_lep3_pt = eem_ZZZ['lep3_pt'].to_numpy()
ttbarG_lep3_pt = eem_ttbarG['lep3_pt'].to_numpy()


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
stak_Z = [ZZZ_Dilep_mass, WZZ_Dilep_mass, WWZ_Dilep_mass, WWW_Dilep_mass, WG_Dilep_mass, ZG_Dilep_mass, ZZ_Dilep_mass, WZ_Dilep_mass, WW_Dilep_mass, ttbarG_Dilep_mass, WZG_Dilep_mass]

stak_MT = [np.clip(ZZZ_MT,0,300,ZZZ_MT), np.clip(WZZ_MT,0,300,WZZ_MT), np.clip(WWZ_MT,0,300,WWZ_MT) , np.clip(WWW_MT,0,300,WWW_MT), np.clip(WG_MT,0,300,WG_MT), np.clip(ZG_MT,0,300,ZG_MT), np.clip(ZZ_MT,0,300,ZZ_MT), np.clip(WZ_MT,0,300,WZ_MT), np.clip(WW_MT,0,300,WW_MT), np.clip(ttbarG_MT,0,300,ttbarG_MT), np.clip(WZG_MT,0,300,WZG_MT)]

stak_pho = [np.clip(ZZZ_pho,0,600,ZZZ_pho), np.clip(WZZ_pho,0,600,WZZ_pho), np.clip(WWZ_pho,0,600,WWZ_pho) , np.clip(WWW_pho,0,600,WWW_pho), np.clip(WG_pho,0,600,WG_pho), np.clip(ZG_pho,0,600,ZG_pho), np.clip(ZZ_pho,0,600,ZZ_pho), np.clip(WZ_pho,0,600,WZ_pho), np.clip(WW_pho,0,600,WW_pho), np.clip(ttbarG_pho,0,600,ttbarG_pho), np.clip(WZG_pho,0,600,WZG_pho)]

stak_MET = [np.clip(ZZZ_MET,0,500,ZZZ_MET), np.clip(WZZ_MET,0,500,WZZ_MET), np.clip(WWZ_MET,0,500,WWZ_MET) , np.clip(WWW_MET,0,500,WWW_MET), np.clip(WG_MET,0,500,WG_MET), np.clip(ZG_MET,0,500,ZG_MET), np.clip(ZZ_MET,0,500,ZZ_MET), np.clip(WZ_MET,0,500,WZ_MET), np.clip(WW_MET,0,500,WW_MET), np.clip(ttbarG_MET,0,500,ttbarG_MET), np.clip(WZG_MET,0,500,WZG_MET)]

stak_triM = [np.clip(ZZZ_Trilep_mass,0,1500,ZZZ_Trilep_mass), np.clip(WZZ_Trilep_mass,0,1500,WZZ_Trilep_mass), np.clip(WWZ_Trilep_mass,0,1500,WWZ_Trilep_mass) , np.clip(WWW_Trilep_mass,0,1500,WWW_Trilep_mass), np.clip(WG_Trilep_mass,0,1500,WG_Trilep_mass), np.clip(ZG_Trilep_mass,0,1500,ZG_Trilep_mass), np.clip(ZZ_Trilep_mass,0,1500,ZZ_Trilep_mass), np.clip(WZ_Trilep_mass,0,1500,WZ_Trilep_mass), np.clip(WW_Trilep_mass,0,1500,WW_Trilep_mass), np.clip(ttbarG_Trilep_mass,0,1500,ttbarG_Trilep_mass), np.clip(WZG_Trilep_mass,0,1500,WZG_Trilep_mass)]

stak_lep1_pt = [np.clip(ZZZ_lep1_pt,0,600,ZZZ_lep1_pt), np.clip(WZZ_lep1_pt,0,600,WZZ_lep1_pt), np.clip(WWZ_lep1_pt,0,600,WWZ_lep1_pt) , np.clip(WWW_lep1_pt,0,600,WWW_lep1_pt), np.clip(WG_lep1_pt,0,600,WG_lep1_pt), np.clip(ZG_lep1_pt,0,600,ZG_lep1_pt), np.clip(ZZ_lep1_pt,0,600,ZZ_lep1_pt), np.clip(WZ_lep1_pt,0,600,WZ_lep1_pt), np.clip(WW_lep1_pt,0,600,WW_lep1_pt), np.clip(ttbarG_lep1_pt,0,600,ttbarG_lep1_pt), np.clip(WZG_lep1_pt,0,600,WZG_lep1_pt)]

stak_lep2_pt = [np.clip(ZZZ_lep2_pt,0,250,ZZZ_lep2_pt), np.clip(WZZ_lep2_pt,0,250,WZZ_lep2_pt), np.clip(WWZ_lep2_pt,0,250,WWZ_lep2_pt) , np.clip(WWW_lep2_pt,0,250,WWW_lep2_pt), np.clip(WG_lep2_pt,0,250,WG_lep2_pt), np.clip(ZG_lep2_pt,0,250,ZG_lep2_pt), np.clip(ZZ_lep2_pt,0,250,ZZ_lep2_pt), np.clip(WZ_lep2_pt,0,250,WZ_lep2_pt), np.clip(WW_lep2_pt,0,250,WW_lep2_pt), np.clip(ttbarG_lep2_pt,0,250,ttbarG_lep2_pt), np.clip(WZG_lep2_pt,0,250,WZG_lep2_pt)]

stak_lep3_pt = [np.clip(ZZZ_lep3_pt,0,400,ZZZ_lep3_pt), np.clip(WZZ_lep3_pt,0,400,WZZ_lep3_pt), np.clip(WWZ_lep3_pt,0,400,WWZ_lep3_pt) , np.clip(WWW_lep3_pt,0,400,WWW_lep3_pt), np.clip(WG_lep3_pt,0,400,WG_lep3_pt), np.clip(ZG_lep3_pt,0,400,ZG_lep3_pt), np.clip(ZZ_lep3_pt,0,400,ZZ_lep3_pt), np.clip(WZ_lep3_pt,0,400,WZ_lep3_pt), np.clip(WW_lep3_pt,0,400,WW_lep3_pt), np.clip(ttbarG_lep3_pt,0,400,ttbarG_lep3_pt), np.clip(WZG_lep3_pt,0,400,WZG_lep3_pt)]

we = [scales["ZZZ"], scales["WZZ"], scales["WWZ"], scales["WWW"], scales["WG"], scales["ZG"], scales["ZZ"], scales["WZ"], scales["WW"], scales["ttbarG"], scales["WZG"]]
co = ['springgreen', 'springgreen', 'springgreen', 'springgreen', 'magenta', 'magenta', 'blue', 'blue', 'blue', 'yellow', 'cyan']
la = ['Tri-Boson', '', '', '', 'V+$\gamma$', '', 'Di-Boson', '', '', 'ttbar+$\gamma$', 'WZ$\gamma$(signal)']

# Z MASS
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_Z[:-1])), range=(81.1876, 101.1876), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_Z)), range=(81.1876, 101.1876), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')
plt.hist(stak_Z, range=(81.1876, 101.1876), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 70)
plt.text(82, 63, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("$M_{ee}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 2 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.savefig("eem_Dilep_mass")
plt.show()
plt.close()

# MT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_MT[:-1])), range=(0, 300), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_MT)), range=(0, 300), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')
plt.hist(stak_MT, range=(0, 300), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 300)
plt.ylim(0, 70)
plt.text(100, 63, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 30 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.savefig("eem_MT")
plt.show()
plt.close()

# Photon PT
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_pho[:-1])), range=(0, 600), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_pho)), range=(0, 600), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_pho, range=(0, 600), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 600)
plt.ylim(0.1, 1000)
plt.text(130, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("Photon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 60 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.yscale('log')
plt.savefig("eem_phopt")
plt.show()
plt.close()

# MET
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_MET[:-1])), range=(0, 500), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_MET)), range=(0, 500), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_MET, range=(0, 500), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0.1, 1000)
plt.text(140, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("$E_{T}^{miss}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 50 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.yscale('log')
plt.savefig("eem_MET")
plt.show()
plt.close()

# Trilep Mass
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_triM[:-1])), range=(0, 1500), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_triM)), range=(0, 1500), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_triM, range=(0, 1500), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 1500)
plt.ylim(0.1, 1000)
plt.text(300, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("$M_{ee\mu}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 150 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.yscale('log')
plt.savefig("eem_Trilep_mass")
plt.show()
plt.close()

# Leading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_lep1_pt[:-1])), range=(0, 600), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_lep1_pt)), range=(0, 600), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_lep1_pt, range=(0, 600), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 600)
plt.ylim(0.1, 1000)
plt.text(150, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("Leading Electron $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 60 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')
plt.yscale('log')
plt.savefig("eem_lep1_pt")
plt.show()
plt.close()

# Subleading lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_lep2_pt[:-1])), range=(0, 250), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_lep2_pt)), range=(0, 250), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_lep2_pt, range=(0, 250), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 250)
plt.ylim(0.1, 1000)
plt.text(75, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("Sub-leading Electron $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 25 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')

plt.yscale('log')
plt.savefig("eem_lep2_pt")
plt.show()
plt.close()

# Third lepton pt
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(np.concatenate((stak_lep3_pt[:-1])), range=(0, 400), alpha=1,linewidth=2.5, weights=np.concatenate((we[:-1])), bins=10, color='black', label="Only Background", stacked=True,histtype='step')
plt.hist(np.concatenate((stak_lep3_pt)), range=(0, 400), alpha=1,linewidth=2.5, weights=np.concatenate((we)), bins=10, color='red', label="Include WZ$\gamma$", stacked=True,histtype='step')

plt.hist(stak_lep3_pt, range=(0, 400), alpha=0.7, weights=we, bins=10, color=co, label=la, stacked=True)
plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 400)
plt.ylim(0.1, 1000)
plt.text(130, 500, '($ee\mu$ channel)', fontsize=20)
plt.xlabel("Third Muon $p_{T}$ [GeV]",fontsize=20, loc='center')
plt.ylabel("Expected Yield | 40 GeV",fontsize=20, loc='center')
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels,fontsize=12,loc='upper right')

plt.yscale('log')
plt.savefig("eem_lep3_pt")
plt.show()
plt.close()

