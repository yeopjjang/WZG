import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy

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

eee_SF = 113.18418333736903
eem_SF = 139.68206865609733
emm_SF = 122.64550324187961
mmm_SF = 137.12107889049585
lumi = 3000000
genevt = 9899604
xsex = 0.00173

plt.rcParams['figure.figsize'] = (8,8)

eee_hbkg = plt.hist(eee_df_bkg['prediction'], histtype='step', weights=eee_df_bkg['weight']*5/eee_SF, bins=50,linewidth=3, color='crimson', label='Background')
eee_hsig = plt.hist(eee_df_sig['prediction'], histtype='step', weights=eee_df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')
plt.axvline(x=0.82, color='black', linestyle=':', linewidth=2, label='Threshold')
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Expected Number of Events', fontsize=17)
plt.ylim(0.1, 1000)
plt.text(0.3, 300, '(eee channel)', fontsize=20)
plt.legend(fontsize=14, loc='upper left')
plt.yscale('log')
plt.savefig("eee_Nor_DNN_score.png")
plt.show()
plt.close()

eem_hbkg = plt.hist(eem_df_bkg['prediction'], histtype='step', weights=eem_df_bkg['weight']*5/eem_SF, bins=50,linewidth=3, color='crimson', label='Background')
eem_hsig = plt.hist(eem_df_sig['prediction'], histtype='step', weights=eem_df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')
plt.axvline(x=0.72, color='black', linestyle=':', linewidth=2, label='Threshold')
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Expected Number of Events', fontsize=17)
plt.ylim(0.1, 1000)
plt.text(0.3, 300, '(ee$\mu$ channel)', fontsize=20)
plt.legend(fontsize=14, loc='upper left')
plt.yscale('log')
plt.savefig("eem_Nor_DNN_score.png")
plt.show()
plt.close()

emm_hbkg = plt.hist(emm_df_bkg['prediction'], histtype='step', weights=emm_df_bkg['weight']*5/emm_SF, bins=50,linewidth=3, color='crimson', label='Background')
emm_hsig = plt.hist(emm_df_sig['prediction'], histtype='step', weights=emm_df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')
plt.axvline(x=0.98, color='black', linestyle=':', linewidth=2, label='Threshold')
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Expected Number of Events', fontsize=17)
plt.ylim(0.1, 1000)
plt.text(0.3, 100, '(e$\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize=14, loc='upper center')
plt.yscale('log')
plt.savefig("emm_Nor_DNN_score.png")
plt.show()
plt.close()

mmm_hbkg = plt.hist(mmm_df_bkg['prediction'], histtype='step', weights=mmm_df_bkg['weight']*5/mmm_SF, bins=50,linewidth=3, color='crimson', label='Background')
mmm_hsig = plt.hist(mmm_df_sig['prediction'], histtype='step', weights=mmm_df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')
plt.axvline(x=0.86, color='black', linestyle=':', linewidth=2, label='Threshold')
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Normalized Expected Number of Events', fontsize=17)
plt.ylim(0.1, 10000)
plt.text(0.4, 3000, '($\mu\mu\mu$ channel)', fontsize=20)
plt.legend(fontsize=14, loc='upper left')
plt.yscale('log')
plt.savefig("mmm_Nor_DNN_score.png")
plt.show()
plt.close()
'''
plt.plot(eee_fpr, eee_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", eee_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
#plt.savefig("eee_ROC.png")
plt.close()

plt.plot(eem_fpr, eem_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", eem_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
#plt.savefig("eem_ROC.png")
plt.close()

plt.plot(emm_fpr, emm_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", emm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
#plt.savefig("emm_ROC.png")
plt.close()

plt.plot(mmm_fpr, mmm_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", mmm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
#plt.savefig("mmm_ROC.png")
plt.close()
'''
eee_N_bkg = eee_hbkg[0]
eee_N_sig = eee_hsig[0]

eem_N_bkg = eem_hbkg[0]
eem_N_sig = eem_hsig[0]

emm_N_bkg = emm_hbkg[0]
emm_N_sig = emm_hsig[0]

mmm_N_bkg = mmm_hbkg[0]
mmm_N_sig = mmm_hsig[0]



#Score = list([round(i*0.02, 2) for i in range(0,50)])

import math
eee_arr_sig, eem_arr_sig, emm_arr_sig, mmm_arr_sig = [],[],[],[]

for cut in range(0,len(eee_N_bkg),1):
	eee_sig_integral = sum(eee_N_sig[cut:])
	eee_bkg_integral = sum(eee_N_bkg[cut:])
	if eee_sig_integral + eee_bkg_integral == 0:
		significance = 0
	else:
		significance = eee_sig_integral / math.sqrt(eee_sig_integral + eee_bkg_integral)
	eee_arr_sig.append(significance)
	print(cut, eee_sig_integral, eee_bkg_integral, significance)

print(eee_arr_sig.index(max(eee_arr_sig)))
print(max(eee_arr_sig))

for cut in range(0,len(eem_N_bkg),1):
        eem_sig_integral = sum(eem_N_sig[cut:])
        eem_bkg_integral = sum(eem_N_bkg[cut:])
        if eem_sig_integral + eem_bkg_integral == 0:
                significance = 0
        else:
                significance = eem_sig_integral / math.sqrt(eem_sig_integral + eem_bkg_integral)
        eem_arr_sig.append(significance)

print(eem_arr_sig.index(max(eem_arr_sig)))
print(max(eem_arr_sig))

for cut in range(0,len(emm_N_bkg),1):
        emm_sig_integral = sum(emm_N_sig[cut:])
        emm_bkg_integral = sum(emm_N_bkg[cut:])
        if emm_sig_integral + emm_bkg_integral == 0:
                significance = 0
        else:
                significance = emm_sig_integral / math.sqrt(emm_sig_integral + emm_bkg_integral)
        emm_arr_sig.append(significance)

print(emm_arr_sig.index(max(emm_arr_sig)))
print(max(emm_arr_sig))

for cut in range(0,len(mmm_N_bkg),1):
        mmm_sig_integral = sum(mmm_N_sig[cut:])
        mmm_bkg_integral = sum(mmm_N_bkg[cut:])
        if mmm_sig_integral + mmm_bkg_integral == 0:
                significance = 0
        else:
                significance = mmm_sig_integral / math.sqrt(mmm_sig_integral + mmm_bkg_integral)
        mmm_arr_sig.append(significance)

print(mmm_arr_sig.index(max(mmm_arr_sig)))
print(max(mmm_arr_sig))

#plt.rcParams["legend.loc"] = 'lower left'
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eee_arr_sig,'--',color='red', label='eee channel', linewidth=2)
#plt.xlabel('DNN score',fontsize=25)
#plt.ylabel('Expected Significance',fontsize=25)
#plt.text(0.2, 1, '(eee_channel)', fontsize=20)
#plt.legend(prop={'size':14})
#plt.grid(which='major', linestyle='-')
#plt.minorticks_on()
#plt.savefig('eee_sig')
#plt.show()
#plt.close()

#plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eem_arr_sig,'-.',color='blue', label='ee$\mu$ channel', linewidth=2)
#plt.xlabel('DNN score',fontsize=25)
#plt.ylabel('Expected Significance',fontsize=25)
#plt.text(0.2, 1.3, '(eem_channel)', fontsize=20)
#plt.legend(prop={'size':14})
#plt.grid(which='major', linestyle='-')
#plt.minorticks_on()
#plt.savefig('eem_sig')
#plt.show()
#plt.close()

#plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),emm_arr_sig,':',color='green', label='e$\mu\mu$ channel', linewidth=2)
#plt.xlabel('DNN score',fontsize=25)
#plt.ylabel('Expected Significance',fontsize=25)
#plt.text(0.2, 1.5, '(emm_channel)', fontsize=20)
#plt.legend(prop={'size':14})
#plt.grid(which='major', linestyle='-')
#plt.minorticks_on()
#plt.savefig('emm_sig')
#plt.show()
#plt.close()

#plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),mmm_arr_sig,'-',color='purple', label='$\mu\mu\mu$ channel', linewidth=2)
plt.xlabel('DNN score',fontsize=20)
plt.ylabel('Expected Significance',fontsize=20)
#plt.text(0.2, 1.5, '(mmm_channel)', fontsize=20)
plt.legend(fontsize=17)
#plt.grid(which='major', linestyle='-')
#plt.minorticks_on()
plt.savefig('sig')
plt.show()
plt.close()


