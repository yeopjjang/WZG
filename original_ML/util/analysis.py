import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy

infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/run/prediction.csv'
#infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/run/data/mix/prediction.csv'


df = pd.read_csv(infile)

tpr, fpr, thr = roc_curve(df['label'], df['prediction'], sample_weight=df['weight'], pos_label=0)
auc = roc_auc_score(df['label'], df['prediction'], sample_weight=df['weight'])

df_bkg = df[df.label == 1]
df_sig = df[df.label == 0]

SF = 11.698375924699228
lumi = 3000000
genevt = 899604
xsex = 0.00173

plt.rcParams['figure.figsize'] = (6,6)

hbkg = plt.hist(df_bkg['prediction'], histtype='step', weights=df_bkg['weight']/SF, bins=50,linewidth=3, color='crimson', label='BKG')
hsig = plt.hist(df_sig['prediction'], histtype='step', weights=df_sig['weight'] * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='SIG')

plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
plt.yscale('log')
plt.savefig("DNN_score.png")
plt.close()

plt.plot(fpr, tpr, '.',linewidth=2, label='%s %.3f' % ("auc", auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("ROC.png")
plt.close()

N_bkg = hbkg[0]
N_sig = hsig[0]
#Score = list([round(i*0.02, 2) for i in range(0,50)])


import math
arr_significance = []
for cut in range(0,len(N_bkg),1):
	sig_integral = sum(N_sig[:cut])
	bkg_integral = sum(N_bkg[:cut])
	if sig_integral+bkg_integral == 0:
		significance = 0
	else:
		significance = sig_integral / math.sqrt(sig_integral + bkg_integral)
	arr_significance.append(significance)
	print(cut, sig_integral, bkg_integral, significance)

print(arr_significance.index(max(arr_significance)))
print(max(arr_significance))

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),arr_significance,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('sig')

