import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

emm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/512neuron/more/emm/prediction.csv'

emm_df = pd.read_csv(emm_infile)

emm_cut_df = emm_df[emm_df['prediction'] >= 0.58]

emm_idx = emm_cut_df.iloc[:,[0]].values.flatten()

emm_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/512neuron/more/emm/emm_testset.h5'

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

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_Dilep_mass, alpha=0.7, bins=40, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(81.1876, 101.1876)
plt.ylim(0, 3100)
plt.text(82, 2800, '(emm channel)', fontsize=20)
plt.xlabel("M(mm) [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 0.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("emm_sig_Z")
plt.show()
plt.close()

plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
bins = np.linspace(0,50,100)
plt.hist(WZG_MT, alpha=0.7, bins=200, color='dodgerblue')
#plt.title("$\sqrt{s}=14 TeV, L=3000 fb^{-1}$", fontsize=13, loc='right')
plt.xlim(0, 500)
plt.ylim(0, 3000)
plt.text(300, 2500, '(emm channel)', fontsize=20)
plt.xlabel("$M_{T}$ [GeV]",fontsize=15, loc='center')
plt.ylabel("Expected Number of Events | 2.5 GeV",fontsize=15, loc='center')
plt.legend(fontsize=12, loc='upper right')
#plt.yscale('log')
plt.savefig("emm_sig_MT")
plt.show()
plt.close()

