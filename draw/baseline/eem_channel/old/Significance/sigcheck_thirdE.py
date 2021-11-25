import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep

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

# Data load
Data = '/x4/cms/dylee/Delphes/analysis/ntuple/eem_channel.npy'

eem_channel = np.load(Data,allow_pickle=True)[()]

WZG = eem_channel['WZG']
WG = eem_channel['WG']
ZG = eem_channel['ZG']
WW = eem_channel['WW']
WZ = eem_channel['WZ']
ZZ = eem_channel['ZZ']
WWW = eem_channel['WWW']
WWZ = eem_channel['WWZ']
WZZ = eem_channel['WZZ']
ZZZ = eem_channel['ZZZ']
ttbarG = eem_channel['ttbarG']

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


# Photon pt
x1 = []
y1 = []

for i in range(0, 200, 1):

	WZG_mask = (WZG.lep3_E > i) #& (ht_tt > j)
	WZG = WZG[WZG_mask]
		
	WG_mask = (WG.lep3_E > i) #& (ht_ttV > j)
	WG = WG[WG_mask]

	ZG_mask = (ZG.lep3_E > i) #& (ht_dy > j)
	ZG = ZG[ZG_mask]

	WW_mask = (WW.lep3_E > i) #& (ht_ww > j)
	WW = WW[WW_mask]

	WZ_mask = (WZ.lep3_E > i) #& (ht_wz > j)
	WZ = WZ[WZ_mask]

	ZZ_mask = (ZZ.lep3_E > i) #& (ht_zz > j)
	ZZ = ZZ[ZZ_mask]

	WWW_mask = (WWW.lep3_E > i) #& (ht_st > j)
	WWW = WWW[WWW_mask]

	WWZ_mask = (WWZ.lep3_E > i) #& (ht_dm > j)
	WWZ = WWZ[WWZ_mask]

	WZZ_mask = (WZZ.lep3_E > i) #& (ht_dm > j)
	WZZ = WZZ[WZZ_mask]

	ZZZ_mask = (ZZZ.lep3_E > i) #& (ht_dm > j)
	ZZZ = ZZZ[ZZZ_mask]

	ttbarG_mask = (ttbarG.lep3_E > i) #& (ht_dm > j)
	ttbarG = ttbarG[ttbarG_mask]

	wght_WZG = len(WZG) * lumi * (xsecDict["WZG"] / EventDict['WZG'])
	wght_WG = len(WG) * lumi * (xsecDict["WG"] / EventDict['WG'])
	wght_ZG = len(ZG) * lumi * xsecDict["ZG"] / EventDict['ZG']
	wght_WW = len(WW) * lumi * xsecDict["WW"] / EventDict['WW']
	wght_WZ = len(WZ) * lumi * xsecDict["WZ"] / EventDict['WZ']
	wght_ZZ = len(ZZ) * lumi * xsecDict["ZZ"] / EventDict['ZZ']
	wght_WWW = len(WWW) * lumi * xsecDict["WWW"] / EventDict['WWW']
	wght_WWZ = len(WWZ) * lumi * xsecDict["WWZ"] / EventDict['WWZ']
	wght_WZZ = len(WZZ) * lumi * xsecDict["WZZ"] / EventDict['WZZ']
	wght_ZZZ = len(ZZZ) * lumi * xsecDict["ZZZ"] / EventDict['ZZZ']
	wght_ttbarG =  len(ttbarG) * lumi * xsecDict["ttbarG"] / EventDict['ttbarG']

	bkg = (wght_WG + wght_ZG + wght_WW + wght_WZ + wght_ZZ + wght_WWW + wght_WWZ + wght_WZZ + wght_ZZZ + wght_ttbarG)

	signal = wght_WZG
	sig = signal / np.sqrt(bkg)

	if 0 <= sig <= 1000:
	
		x1.append(i)
		y1.append(sig)
		print("# sig: {0} # bkg: {1} # sigma: {2} # Cut: {3}".format(signal,bkg,sig,i))

print("Max sig : {0}".format(max(y1)))	

# Draw hist
plt.figure(figsize=(8,8))
plt.style.use(hep.style.CMS)
plt.plot(x1,y1, color='royalblue', linewidth=3)
plt.title("Third Lepton Energy", fontsize=30, loc='center')
plt.xlabel("Cut Value | 1 GeV",fontsize=15, loc='center')
plt.ylabel("Expected Significance",fontsize=15, loc='center')
plt.savefig("lep3_E")
plt.show()

