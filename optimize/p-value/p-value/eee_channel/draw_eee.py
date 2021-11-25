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

p_value = GetPvalue(125.72, 30.99+125.72)
print(p_value)

bkg = 125.72
sig = 30.99

array = np.arange(2*(sig+bkg))
test = poisson(bkg).pmf(array)
array2 = np.arange(sig+bkg)
test2 = poisson(sig+bkg).pmf(array)

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)

plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(180, 0.030, '(eee channel)', fontsize=17)
plt.xlim(75,225)
plt.ylim(0, 0.040)
plt.legend(fontsize=15, loc='upper right')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("eee_linear")
plt.show()
plt.close()

plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)

plt.plot(test, color='blue', label='Only Background', linewidth=2.0)
plt.fill_between(array, test, where=array>=sig+bkg, color='red', label='P-Value')
plt.plot(test2, color='black', label='Signal + Background', linewidth=2.0)
plt.text(300, 10e-6, '(eee channel)', fontsize=17)
plt.xlim(0,400)
plt.ylim(10e-25, 10)
plt.legend(fontsize=15, loc='upper right')
plt.yscale('log')
plt.xlabel('Number of Expected Events', fontsize=20, loc='center')
plt.ylabel('Probability', fontsize=20, loc='center')
plt.savefig("eee_log")
plt.show()


eee_sig = ROOT.Math.gaussian_quantile_c(p_value,1)
print(eee_sig)
