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

p_value = GetPvalue(447.48, 79.97+447.48)
print(p_value)

bkg = 447.48
sig = 79.97

array = np.arange(2*(sig+bkg))
test = poisson(bkg).pmf(array)
array2 = np.arange(sig+bkg)
test2 = poisson(sig+bkg).pmf(array)

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(560, 0.015, '(e$\mu\mu$ channel)', fontsize=17)
plt.xlim(350,650)
plt.ylim(0, 0.021)
plt.legend(fontsize=15, loc='upper right')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("emm_linear")
plt.show()
plt.close()

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(700, 10e-6, '(e$\mu\mu$ channel)', fontsize=17)
plt.xlim(200,900)
plt.ylim(10e-25, 10)
plt.legend(fontsize=15, loc='upper right')
plt.yscale('log')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("emm_log")
plt.show()

emm_sig = ROOT.Math.gaussian_quantile_c(p_value,1)

print(emm_sig)
