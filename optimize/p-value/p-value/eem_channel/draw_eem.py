import scipy
import ROOT
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep


def GetPvalue(nbkg,ntotal):
	x = np.arange(ntotal) # H0 prob var array upto H1 mean
	bkg = nbkg
	y = poisson(bkg).pmf(x)
	p_value = 1 - y.sum()
	return p_value

p_value = GetPvalue(189.33, 48.47+189.33)
print(p_value)

bkg = 189.33
sig = 48.47

array = np.arange(2*(sig+bkg))
test = poisson(bkg).pmf(array)
array2 = np.arange(sig+bkg)
test2 = poisson(sig+bkg).pmf(array)

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(250, 0.025, '(ee$\mu$ channel)', fontsize=17)
plt.xlim(120,320)
plt.ylim(0, 0.035)
plt.legend(fontsize=15, loc='upper right')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("eem_linear")
plt.show()
plt.close()

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(350, 10e-7, '(ee$\mu$ channel)', fontsize=17)
plt.xlim(0,500)
plt.ylim(10e-25, 10)
plt.legend(fontsize=15, loc='upper right')
plt.yscale('log')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("eem_log")
plt.show()


eem_sig = ROOT.Math.gaussian_quantile_c(p_value,1)
print(eem_sig)
