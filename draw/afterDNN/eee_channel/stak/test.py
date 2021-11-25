import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

eee_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/run/much/eee/prediction.csv'

eee_df = pd.read_csv(eee_infile)

eee_cut_df = eee_df[eee_df['prediction'] >= 0.68]

eee_idx = eee_cut_df.iloc[:,[0]].values.flatten()

eee_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/run/much/eee/eee_testset.h5'

eee_test_df = pd.read_hdf(eee_testset)

eee_after = eee_test_df.iloc[eee_idx]

eee_WZG = eee_after[eee_after['xsec'] == 0.00173]
eee_WG = eee_after[eee_after['xsec'] == 23.08]
eee_ZG = eee_after[eee_after['xsec'] == 4.977]
eee_WW = eee_after[eee_after['xsec'] == 3.356]
eee_WZ = eee_after[eee_after['xsec'] == 0.3983]
eee_ZZ = eee_after[eee_after['xsec'] == 0.04642]
eee_WWW = eee_after[eee_after['xsec'] == 0.001335]
eee_WWZ = eee_after[eee_after['xsec'] == 0.0003067]
eee_WZZ = eee_after[eee_after['xsec'] == 0.00002989]
eee_ZZZ = eee_after[eee_after['xsec'] == 0.000003157]
eee_ttbarG = eee_after[eee_after['xsec'] == 2.445]

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
WZG_Dilep_mass = eee_WZG['dilep_mass'].to_numpy()
WG_Dilep_mass = eee_WG['dilep_mass'].to_numpy()
ZG_Dilep_mass = eee_ZG['dilep_mass'].to_numpy()
WW_Dilep_mass = eee_WW['dilep_mass'].to_numpy()
WZ_Dilep_mass = eee_WZ['dilep_mass'].to_numpy()
ZZ_Dilep_mass = eee_ZZ['dilep_mass'].to_numpy()
WWW_Dilep_mass = eee_WWW['dilep_mass'].to_numpy()
WWZ_Dilep_mass = eee_WWZ['dilep_mass'].to_numpy()
WZZ_Dilep_mass = eee_WZZ['dilep_mass'].to_numpy()
ZZZ_Dilep_mass = eee_ZZZ['dilep_mass'].to_numpy()
ttbarG_Dilep_mass = eee_ttbarG['dilep_mass'].to_numpy()

WZG_MT = eee_WZG['MT'].to_numpy()
WG_MT = eee_WG['MT'].to_numpy()
ZG_MT = eee_ZG['MT'].to_numpy()
WW_MT = eee_WW['MT'].to_numpy()
WZ_MT = eee_WZ['MT'].to_numpy()
ZZ_MT = eee_ZZ['MT'].to_numpy()
WWW_MT = eee_WWW['MT'].to_numpy()
WWZ_MT = eee_WWZ['MT'].to_numpy()
WZZ_MT = eee_WZZ['MT'].to_numpy()
ZZZ_MT = eee_ZZZ['MT'].to_numpy()
ttbarG_MT = eee_ttbarG['MT'].to_numpy()

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, alpha=0.7, bins=40, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 1200)
plt.text(82, 1100, '(eee channel)', fontsize=20)
plt.xlabel("M(ee) [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 0.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.savefig("eee_sig_Z")
plt.show()
plt.close()

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, alpha=0.7, bins=200, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0, 1300)
plt.text(300, 1100, '(eee channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 2.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
plt.savefig("eee_sig_MT")
plt.show()
plt.close()

