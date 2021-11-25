import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

eem_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/1024neuron/less/eem/prediction.csv'

eem_df = pd.read_csv(eem_infile)

eem_cut_df = eem_df[eem_df['prediction'] >= 0.58]

eem_idx = eem_cut_df.iloc[:,[0]].values.flatten()

eem_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/1024neuron/less/eem/eem_testset.h5'

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

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, alpha=0.7, bins=50, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 1500)
plt.text(82, 1300, '(eem channel)', fontsize=20)
plt.xlabel("M(ee) [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 0.4 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("eem_sig_Z")
plt.show()
plt.close()

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, alpha=0.7, bins=200, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0, 2000)
plt.text(300, 1800, '(eem channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 2.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("eem_sig_MT")
plt.show()
plt.close()

