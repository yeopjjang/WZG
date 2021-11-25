import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

mmm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/1024neuron/much/mmm/prediction.csv'

mmm_df = pd.read_csv(mmm_infile)

mmm_cut_df = mmm_df[mmm_df['prediction'] >= 0.86]

mmm_idx = mmm_cut_df.iloc[:,[0]].values.flatten()

mmm_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/1024neuron/much/mmm/mmm_testset.h5'

mmm_test_df = pd.read_hdf(mmm_testset)

mmm_after = mmm_test_df.iloc[mmm_idx]

mmm_WZG = mmm_after[mmm_after['xsec'] == 0.00173]
mmm_WG = mmm_after[mmm_after['xsec'] == 23.08]
mmm_ZG = mmm_after[mmm_after['xsec'] == 4.977]
mmm_WW = mmm_after[mmm_after['xsec'] == 3.356]
mmm_WZ = mmm_after[mmm_after['xsec'] == 0.3983]
mmm_ZZ = mmm_after[mmm_after['xsec'] == 0.04642]
mmm_WWW = mmm_after[mmm_after['xsec'] == 0.001335]
mmm_WWZ = mmm_after[mmm_after['xsec'] == 0.0003067]
mmm_WZZ = mmm_after[mmm_after['xsec'] == 0.00002989]
mmm_ZZZ = mmm_after[mmm_after['xsec'] == 0.000003157]
mmm_ttbarG = mmm_after[mmm_after['xsec'] == 2.445]

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
WZG_Dilep_mass = mmm_WZG['dilep_mass'].to_numpy()
WG_Dilep_mass = mmm_WG['dilep_mass'].to_numpy()
ZG_Dilep_mass = mmm_ZG['dilep_mass'].to_numpy()
WW_Dilep_mass = mmm_WW['dilep_mass'].to_numpy()
WZ_Dilep_mass = mmm_WZ['dilep_mass'].to_numpy()
ZZ_Dilep_mass = mmm_ZZ['dilep_mass'].to_numpy()
WWW_Dilep_mass = mmm_WWW['dilep_mass'].to_numpy()
WWZ_Dilep_mass = mmm_WWZ['dilep_mass'].to_numpy()
WZZ_Dilep_mass = mmm_WZZ['dilep_mass'].to_numpy()
ZZZ_Dilep_mass = mmm_ZZZ['dilep_mass'].to_numpy()
ttbarG_Dilep_mass = mmm_ttbarG['dilep_mass'].to_numpy()

WZG_MT = mmm_WZG['MT'].to_numpy()
WG_MT = mmm_WG['MT'].to_numpy()
ZG_MT = mmm_ZG['MT'].to_numpy()
WW_MT = mmm_WW['MT'].to_numpy()
WZ_MT = mmm_WZ['MT'].to_numpy()
ZZ_MT = mmm_ZZ['MT'].to_numpy()
WWW_MT = mmm_WWW['MT'].to_numpy()
WWZ_MT = mmm_WWZ['MT'].to_numpy()
WZZ_MT = mmm_WZZ['MT'].to_numpy()
ZZZ_MT = mmm_ZZZ['MT'].to_numpy()
ttbarG_MT = mmm_ttbarG['MT'].to_numpy()
'''
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, alpha=0.7, bins=40, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 3500)
plt.text(82, 3200, '(mmm channel)', fontsize=20)
plt.xlabel("M(mm) [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 0.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("mmm_sig_Z")
plt.show()
plt.close()
'''
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, alpha=0.7, bins=200, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0, 2500)
plt.text(300, 2300, '(mmm channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 2.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("mmm_sig_MT")
plt.show()
plt.close()

