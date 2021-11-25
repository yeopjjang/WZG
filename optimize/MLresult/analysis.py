import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy
#import mplhep as hep

eee_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/less/eee/prediction.csv'
eem_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/more/eem/prediction.csv'
emm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/1024neuron/most/emm/prediction.csv'
mmm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/4096neuron/much/mmm/prediction.csv'

eee_df = pd.read_csv(eee_infile)
eem_df = pd.read_csv(eem_infile)
emm_df = pd.read_csv(emm_infile)
mmm_df = pd.read_csv(mmm_infile)

eee_tpr, eee_fpr, eee_thr = roc_curve(eee_df['label'], eee_df['prediction'], sample_weight=eee_df['weight'], pos_label=0)
eem_tpr, eem_fpr, eem_thr = roc_curve(eem_df['label'], eem_df['prediction'], sample_weight=eem_df['weight'], pos_label=0)
emm_tpr, emm_fpr, emm_thr = roc_curve(emm_df['label'], emm_df['prediction'], sample_weight=emm_df['weight'], pos_label=0)
mmm_tpr, mmm_fpr, mmm_thr = roc_curve(mmm_df['label'], mmm_df['prediction'], sample_weight=mmm_df['weight'], pos_label=0)

eee_auc = roc_auc_score(eee_df['label'], eee_df['prediction'], sample_weight=eee_df['weight'])
eem_auc = roc_auc_score(eem_df['label'], eem_df['prediction'], sample_weight=eem_df['weight'])
emm_auc = roc_auc_score(emm_df['label'], emm_df['prediction'], sample_weight=emm_df['weight'])
mmm_auc = roc_auc_score(mmm_df['label'], mmm_df['prediction'], sample_weight=mmm_df['weight'])

eee_df_bkg = eee_df[eee_df.label == 0]
eee_df_sig = eee_df[eee_df.label == 1]

eem_df_bkg = eem_df[eem_df.label == 0]
eem_df_sig = eem_df[eem_df.label == 1]

emm_df_bkg = emm_df[emm_df.label == 0]
emm_df_sig = emm_df[emm_df.label == 1]

mmm_df_bkg = mmm_df[mmm_df.label == 0]
mmm_df_sig = mmm_df[mmm_df.label == 1]

eee_SF = 10.458301622766731
eem_SF = 20.366929671269794
emm_SF = 18.407198288188823
mmm_SF = 13.76974571541884
lumi = 3000000
genevt = 9899604
xsex = 0.00173

plt.rcParams['figure.figsize'] = (8,8)

eee_hbkg = plt.hist(eee_df_bkg['prediction'], histtype='step', weights=eee_df_bkg['weight'], bins=50, linewidth=3, color='crimson', label='Background')
eee_hsig = plt.hist(eee_df_sig['prediction'], histtype='step', weights=eee_df_sig['weight'], bins=50, linewidth=3, color='royalblue', label='Signal')
#plt.axvline(x=0.68, color='black', linestyle=':', linewidth=2, label='Optimize Point')
plt.xlabel('DNN score', fontsize=17, loc='center')
plt.ylabel('Rescaled Number of Events', fontsize=17, loc='center')
plt.text(0.2, 4000, '(eee channel)', fontsize=20, family="Comic Sans MS")
plt.ylim(0,4500)
plt.legend(fontsize=15)
plt.savefig("eee_DNN_score.png")
plt.show()
plt.close()

eem_hbkg = plt.hist(eem_df_bkg['prediction'], histtype='step', weights=eem_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='Background')
eem_hsig = plt.hist(eem_df_sig['prediction'], histtype='step', weights=eem_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='Signal')
#plt.axvline(x=0.58, color='black', linestyle=':', linewidth=2, label='Optimize Point')
plt.xlabel('DNN score', fontsize=17, loc='center')
plt.ylabel('Rescaled Number of Events', fontsize=17, loc='center')
plt.text(0.4, 3500, '(ee$\mu$ channel)', fontsize=20, family='Comic Sans MS')
plt.legend(fontsize=15, loc='upper left')
plt.savefig("eem_DNN_score.png")
plt.show()
plt.close()

emm_hbkg = plt.hist(emm_df_bkg['prediction'], histtype='step', weights=emm_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='Background')
emm_hsig = plt.hist(emm_df_sig['prediction'], histtype='step', weights=emm_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='Signal')
#plt.axvline(x=0.58, color='black', linestyle=':', linewidth=2, label='Optimize Point')
plt.xlabel('DNN score', fontsize=17, loc='center')
plt.ylabel('Rescaled Number of Events', fontsize=17, loc='center')
plt.text(0.4, 30000, '(e$\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize=15, loc='upper left')
plt.savefig("emm_DNN_score.png")
plt.show()
plt.close()

mmm_hbkg = plt.hist(mmm_df_bkg['prediction'], histtype='step', weights=mmm_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='Background')
mmm_hsig = plt.hist(mmm_df_sig['prediction'], histtype='step', weights=mmm_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='Signal')
#plt.axvline(x=0.86, color='black', linestyle=':', linewidth=2, label='Optimize Point')
plt.xlabel('DNN score', fontsize=17, loc='center')
plt.ylabel('Rescaled Number of Events', fontsize=17, loc='center')
plt.text(0.4, 26000, '($\mu\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize=15, loc='upper left')
plt.savefig("mmm_DNN_score.png")
plt.show()
plt.close()


plt.plot(eee_fpr, eee_tpr, '.',linewidth=2, label='%s %.3f' % ("AUC", eee_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('1 - Background Rejection', fontsize=17)
plt.ylabel('Signal Efficiency', fontsize=17)
plt.text(0.6, 0.8, '(eee channel)', fontsize=20)
plt.legend(fontsize =17)
plt.savefig("eee_ROC.png")
plt.show()
plt.close()

plt.plot(eem_fpr, eem_tpr, '.',linewidth=2, label='%s %.3f' % ("AUC", eem_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('1 - Background Rejection', fontsize=17)
plt.ylabel('Signal Efficiency', fontsize=17)
plt.text(0.6, 0.8, '(ee$\mu$ channel)', fontsize=20)
plt.legend(fontsize =17)
plt.savefig("eem_ROC.png")
plt.close()

plt.plot(emm_fpr, emm_tpr, '.',linewidth=2, label='%s %.3f' % ("AUC", emm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('1 - Background Rejection', fontsize=17)
plt.ylabel('Signal Efficiency', fontsize=17)
plt.text(0.6, 0.8, '(e$\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize =17)
plt.savefig("emm_ROC.png")
plt.close()

plt.plot(mmm_fpr, mmm_tpr, '.',linewidth=2, label='%s %.3f' % ("AUC", mmm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('1 - Background Rejection', fontsize=17)
plt.ylabel('Signal Efficiency', fontsize=17)
plt.text(0.6, 0.8, '($\mu\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize =17)
plt.savefig("mmm_ROC.png")
plt.close()

eee_N_bkg = eee_hbkg[0]
eee_N_sig = eee_hsig[0]

eem_N_bkg = eem_hbkg[0]
eem_N_sig = eem_hsig[0]

emm_N_bkg = emm_hbkg[0]
emm_N_sig = emm_hsig[0]

mmm_N_bkg = mmm_hbkg[0]
mmm_N_sig = mmm_hsig[0]

#Score = list([round(i*0.02, 2) for i in range(0,50)])
'''
import math
eee_arr_sig, eem_arr_sig, emm_arr_sig, mmm_arr_sig = [],[],[],[]

for cut in range(0,len(eee_N_bkg),1):
	eee_sig_integral = sum(eee_N_sig[:cut])
	eee_bkg_integral = sum(eee_N_bkg[:cut])
	if eee_sig_integral + eee_bkg_integral == 0:
		significance = 0
	else:
		significance = eee_sig_integral / math.sqrt(eee_sig_integral + eee_bkg_integral)
	eee_arr_sig.append(significance)
#	print(cut, eee_sig_integral, eee_bkg_integral, significance)

print(eee_arr_sig.index(max(eee_arr_sig)))
print(max(eee_arr_sig))

for cut in range(0,len(eem_N_bkg),1):
        eem_sig_integral = sum(eem_N_sig[:cut])
        eem_bkg_integral = sum(eem_N_bkg[:cut])
        if eem_sig_integral + eem_bkg_integral == 0:
                significance = 0
        else:
                significance = eem_sig_integral / math.sqrt(eem_sig_integral + eem_bkg_integral)
        eem_arr_sig.append(significance)

print(eem_arr_sig.index(max(eem_arr_sig)))
print(max(eem_arr_sig))

for cut in range(0,len(emm_N_bkg),1):
        emm_sig_integral = sum(emm_N_sig[:cut])
        emm_bkg_integral = sum(emm_N_bkg[:cut])
        if emm_sig_integral + emm_bkg_integral == 0:
                significance = 0
        else:
                significance = emm_sig_integral / math.sqrt(emm_sig_integral + emm_bkg_integral)
        emm_arr_sig.append(significance)

print(emm_arr_sig.index(max(emm_arr_sig)))
print(max(emm_arr_sig))

for cut in range(0,len(mmm_N_bkg),1):
        mmm_sig_integral = sum(mmm_N_sig[:cut])
        mmm_bkg_integral = sum(mmm_N_bkg[:cut])
        if mmm_sig_integral + mmm_bkg_integral == 0:
                significance = 0
        else:
                significance = mmm_sig_integral / math.sqrt(mmm_sig_integral + mmm_bkg_integral)
        mmm_arr_sig.append(significance)

print(mmm_arr_sig.index(max(mmm_arr_sig)))
print(max(mmm_arr_sig))

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eee_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('eee_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eem_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('eem_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),emm_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('emm_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),mmm_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('mmm_sig')
plt.close()


'''
