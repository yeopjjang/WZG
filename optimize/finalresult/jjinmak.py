import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep
import scipy
from scipy.stats import poisson
import ROOT

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

eeeDict ={
"WZG" : 11824,
"WG" : 0,
"ZG" : 0,
"WW" : 1,
"WZ" : 124,
"ZZ" : 348,
"WWW" : 51,
"WWZ" : 727,
"WZZ" : 1037,
"ZZZ" : 727,
"ttbarG" : 6,
}

eemDict ={
"WZG" : 18491,
"WG" : 0,
"ZG" : 1,
"WW" : 0,
"WZ" : 208,
"ZZ" : 242,
"WWW" : 54,
"WWZ" : 969,
"WZZ" : 781,
"ZZZ" : 429,
"ttbarG" : 11,
}

emmDict ={
"WZG" : 30509,
"WG" : 0,
"ZG" : 4,
"WW" : 1,
"WZ" : 365,
"ZZ" : 1572,
"WWW" : 84,
"WWZ" : 1845,
"WZZ" : 2680,
"ZZZ" : 1995,
"ttbarG" : 23,
}

mmmDict ={
"WZG" : 38771,
"WG" : 0,
"ZG" : 7,
"WW" : 1,
"WZ" : 456,
"ZZ" : 676,
"WWW" : 84,
"WWZ" : 2117,
"WZZ" : 1660,
"ZZZ" : 1045,
"ttbarG" : 21,
}

eee_histo = {'lumi':[], 'sig':[], 'pvalue':[]}
eem_histo = {'lumi':[], 'sig':[], 'pvalue':[]}
emm_histo = {'lumi':[], 'sig':[], 'pvalue':[]}
mmm_histo = {'lumi':[], 'sig':[], 'pvalue':[]}
com_histo = {'lumi':[], 'sig':[], 'pvalue':[]}

def GetPvalue(nbkg, ntotal):
	x = np.arange(ntotal)
	bkg = nbkg
	y =poisson(bkg).pmf(x)
	p_value = 1 - y.sum()
	return p_value

#eee
for lumi in range(0, 11010000, 100000):

	# eee Yield
	eee_Yield = {

	"WZG" : eeeDict["WZG"] * lumi * (xsecDict["WZG"] / EventDict['WZG']),
	"WG" : eeeDict["WG"] * lumi * (xsecDict["WG"] / EventDict['WG']),
	"ZG" : eeeDict["ZG"] * lumi * xsecDict["ZG"] / EventDict['ZG'],
	"WW" : eeeDict["WW"] * lumi * xsecDict["WW"] / EventDict['WW'],
	"WZ" : eeeDict["WZ"] * lumi * xsecDict["WZ"] / EventDict['WZ'],
	"ZZ" : eeeDict["ZZ"] * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
	"WWW" : eeeDict["WWW"] * lumi * xsecDict["WWW"] / EventDict['WWW'],
	"WWZ" : eeeDict["WWZ"] * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
	"WZZ" : eeeDict["WZZ"] * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
	"ZZZ" : eeeDict["ZZZ"] * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
	"ttbarG" : eeeDict["ttbarG"] * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

	}

	# eee Significance
	eee_total_bkg = (eee_Yield['WG'] + eee_Yield['ZG'] + eee_Yield['WW'] + eee_Yield['WZ'] + eee_Yield['ZZ'] + eee_Yield['WWW'] + eee_Yield['WWZ'] + eee_Yield['WZZ'] + eee_Yield['ZZZ'] + eee_Yield['ttbarG'])
	
	eee_signal = eee_Yield['WZG']
	
	eee_pvalue = GetPvalue(eee_total_bkg, eee_total_bkg + eee_signal)

	eee_sig = ROOT.Math.gaussian_quantile_c(eee_pvalue,1)

	eee_histo['lumi'].append(lumi/1000)
	eee_histo['pvalue'].append(eee_pvalue)	
	eee_histo['sig'].append(eee_sig)

        # eem Yield
	eem_Yield = {

	"WZG" : eemDict["WZG"] * lumi * (xsecDict["WZG"] / EventDict['WZG']),
	"WG" : eemDict["WG"] * lumi * (xsecDict["WG"] / EventDict['WG']),
	"ZG" : eemDict["ZG"] * lumi * xsecDict["ZG"] / EventDict['ZG'],
	"WW" : eemDict["WW"] * lumi * xsecDict["WW"] / EventDict['WW'],
	"WZ" : eemDict["WZ"] * lumi * xsecDict["WZ"] / EventDict['WZ'],
	"ZZ" : eemDict["ZZ"] * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
	"WWW" : eemDict["WWW"] * lumi * xsecDict["WWW"] / EventDict['WWW'],
	"WWZ" : eemDict["WWZ"] * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
	"WZZ" : eemDict["WZZ"] * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
	"ZZZ" : eemDict["ZZZ"] * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
	"ttbarG" : eemDict["ttbarG"] * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

	}

        # eem Significance
	eem_total_bkg = (eem_Yield['WG'] + eem_Yield['ZG'] + eem_Yield['WW'] + eem_Yield['WZ'] + eem_Yield['ZZ'] + eem_Yield['WWW'] + eem_Yield['WWZ'] + eem_Yield['WZZ'] + eem_Yield['ZZZ'] + eem_Yield['ttbarG'])

	eem_signal = eem_Yield['WZG']

	eem_pvalue = GetPvalue(eem_total_bkg, eem_total_bkg + eem_signal)

	eem_sig = ROOT.Math.gaussian_quantile_c(eem_pvalue,1)

	eem_histo['lumi'].append(lumi/1000)
	eem_histo['pvalue'].append(eem_pvalue)
	eem_histo['sig'].append(eem_sig)

	# emm Yield
	emm_Yield = {

	"WZG" : emmDict["WZG"] * lumi * (xsecDict["WZG"] / EventDict['WZG']),
	"WG" : emmDict["WG"] * lumi * (xsecDict["WG"] / EventDict['WG']),
	"ZG" : emmDict["ZG"] * lumi * xsecDict["ZG"] / EventDict['ZG'],
	"WW" : emmDict["WW"] * lumi * xsecDict["WW"] / EventDict['WW'],
	"WZ" : emmDict["WZ"] * lumi * xsecDict["WZ"] / EventDict['WZ'],
	"ZZ" : emmDict["ZZ"] * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
	"WWW" : emmDict["WWW"] * lumi * xsecDict["WWW"] / EventDict['WWW'],
	"WWZ" : emmDict["WWZ"] * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
	"WZZ" : emmDict["WZZ"] * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
	"ZZZ" : emmDict["ZZZ"] * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
	"ttbarG" : emmDict["ttbarG"] * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

	}

        # emm Significance
	emm_total_bkg = (emm_Yield['WG'] + emm_Yield['ZG'] + emm_Yield['WW'] + emm_Yield['WZ'] + emm_Yield['ZZ'] + emm_Yield['WWW'] + emm_Yield['WWZ'] + emm_Yield['WZZ'] + emm_Yield['ZZZ'] + emm_Yield['ttbarG'])

	emm_signal = emm_Yield['WZG']

	emm_pvalue = GetPvalue(emm_total_bkg, emm_total_bkg + emm_signal)

	emm_sig = ROOT.Math.gaussian_quantile_c(emm_pvalue,1)

	emm_histo['lumi'].append(lumi/1000)
	emm_histo['pvalue'].append(emm_pvalue)
	emm_histo['sig'].append(emm_sig)

	# mmm Yield
	mmm_Yield = {

	"WZG" : mmmDict["WZG"] * lumi * (xsecDict["WZG"] / EventDict['WZG']),
	"WG" : mmmDict["WG"] * lumi * (xsecDict["WG"] / EventDict['WG']),
	"ZG" : mmmDict["ZG"] * lumi * xsecDict["ZG"] / EventDict['ZG'],
	"WW" : mmmDict["WW"] * lumi * xsecDict["WW"] / EventDict['WW'],
	"WZ" : mmmDict["WZ"] * lumi * xsecDict["WZ"] / EventDict['WZ'],
	"ZZ" : mmmDict["ZZ"] * lumi * xsecDict["ZZ"] / EventDict['ZZ'],
	"WWW" : mmmDict["WWW"] * lumi * xsecDict["WWW"] / EventDict['WWW'],
	"WWZ" : mmmDict["WWZ"] * lumi * xsecDict["WWZ"] / EventDict['WWZ'],
	"WZZ" : mmmDict["WZZ"] * lumi * xsecDict["WZZ"] / EventDict['WZZ'],
	"ZZZ" : mmmDict["ZZZ"] * lumi * xsecDict["ZZZ"] / EventDict['ZZZ'],
	"ttbarG" : mmmDict["ttbarG"] * lumi * xsecDict["ttbarG"] / EventDict['ttbarG'],

	}

        # mmm Significance
	mmm_total_bkg = (mmm_Yield['WG'] + mmm_Yield['ZG'] + mmm_Yield['WW'] + mmm_Yield['WZ'] + mmm_Yield['ZZ'] + mmm_Yield['WWW'] + mmm_Yield['WWZ'] + mmm_Yield['WZZ'] + mmm_Yield['ZZZ'] + mmm_Yield['ttbarG'])

	mmm_signal = mmm_Yield['WZG']

	mmm_pvalue = GetPvalue(mmm_total_bkg, mmm_total_bkg + mmm_signal)

	mmm_sig = ROOT.Math.gaussian_quantile_c(mmm_pvalue,1)

	mmm_histo['lumi'].append(lumi/1000)
	mmm_histo['pvalue'].append(mmm_pvalue)
	mmm_histo['sig'].append(mmm_sig)

	# Combine
	com_Yield = {

	"WZG" : eee_Yield['WZG'] + eem_Yield['WZG'] + emm_Yield['WZG'] + mmm_Yield['WZG'],
	"WG" : eee_Yield['WG'] + eem_Yield['WG'] + emm_Yield['WG'] + mmm_Yield['WG'],
	"ZG" : eee_Yield['ZG'] + eem_Yield['ZG'] + emm_Yield['ZG'] + mmm_Yield['ZG'],
	"WW" : eee_Yield['WW'] + eem_Yield['WW'] + emm_Yield['WW'] + mmm_Yield['WW'],
	"WZ" : eee_Yield['WZ'] + eem_Yield['WZ'] + emm_Yield['WZ'] + mmm_Yield['WZ'],
	"ZZ" : eee_Yield['ZZ'] + eem_Yield['ZZ'] + emm_Yield['ZZ'] + mmm_Yield['ZZ'],
	"WWW" : eee_Yield['WWW'] + eem_Yield['WWW'] + emm_Yield['WWW'] + mmm_Yield['WWW'],
	"WWZ" : eee_Yield['WWZ'] + eem_Yield['WWZ'] + emm_Yield['WWZ'] + mmm_Yield['WWZ'],
	"WZZ" : eee_Yield['WZZ'] + eem_Yield['WZZ'] + emm_Yield['WZZ'] + mmm_Yield['WZZ'],
	"ZZZ" : eee_Yield['ZZZ'] + eem_Yield['ZZZ'] + emm_Yield['ZZZ'] + mmm_Yield['ZZZ'],
	"ttbarG" : eee_Yield['ttbarG'] + eem_Yield['ttbarG'] + emm_Yield['ttbarG'] + mmm_Yield['ttbarG'],

	}

	# com Significance
	com_total_bkg = (com_Yield['WG'] + com_Yield['ZG'] + com_Yield['WW'] + com_Yield['WZ'] + com_Yield['ZZ'] + com_Yield['WWW'] + com_Yield['WWZ'] + com_Yield['WZZ'] + com_Yield['ZZZ'] + com_Yield['ttbarG'])

	com_signal = com_Yield['WZG']

	com_pvalue = GetPvalue(com_total_bkg, com_total_bkg + com_signal)

	com_sig = ROOT.Math.gaussian_quantile_c(com_pvalue,1)

	com_histo['lumi'].append(lumi/1000)
	com_histo['pvalue'].append(com_pvalue)
	com_histo['sig'].append(com_sig)
	
	#if com_sig >= 5:
	#	print(lumi/1000)


plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(eee_histo['lumi'], eee_histo['sig'], label='eee channel',color='red', linewidth=2, linestyle='--')
plt.plot(eem_histo['lumi'], eem_histo['sig'], label='ee$\mu$ channel',color='blue', linewidth=2, linestyle='-.')
plt.plot(emm_histo['lumi'], emm_histo['sig'], label='e$\mu\mu$ channel',color='green', linewidth=2, linestyle=':')
plt.plot(mmm_histo['lumi'], mmm_histo['sig'], label='$\mu\mu\mu$ channel',color='purple', linewidth=2, linestyle='-')
plt.plot(com_histo['lumi'], com_histo['sig'], label='combine channel',color='darkslategray', linewidth=3)

plt.axhline(5, 0, 10000, color='black', linestyle='-', linewidth=1, label='5 $\sigma$ line')

plt.legend(fontsize=17, loc='lower right')
plt.xlim(0,11000)
plt.ylim(0,7)
plt.xlabel("Luminosity [$fb^{-1}$]", fontsize=20, loc='center')
plt.ylabel("Expected Significance", fontsize=20, loc='center')

plt.savefig("final_result")
plt.show()










