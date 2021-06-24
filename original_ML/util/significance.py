import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

predFile = 'prediction.csv'

df = pd.read_csv(predFile)

idx_sig = np.where(df['label'] == 0)[0]
idx_bkg = np.where(df['label'] == 1)[0]

pred_sig = df['prediction'][idx_sig]
pred_bkg = df['prediction'][idx_bkg]

print(pred_sig[0])

'''
#N_bkg = pred_bkg[0]
N_sig = pred_sig[0]
Score = list([round(i*0.02,2) for i in range(0,50)])

import math
arr_sig = []
for cut in range(0, len(Score)-1,1):
	sig_integral = sum(N_sig[:cut])
	bkg_integral = sum(N_bkg[:cut])
	
	if sig_integral+bkg_integral == 0:
		significance = 0
	else:
		significance = sig_integral / math.sqrt(sig_integral+bkg_integral)
	arr_sig.append(significance)




	
'''	

