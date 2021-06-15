import torch
from torch import from_numpy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"

df = pd.read_hdf(infile)

for i in df.iloc[:, 3:-2]:
	feature = df['{0}'.format(i)].values
	plt.hist(feature, bins=40, color='royalblue', alpha=0.7)
	plt.xlabel('{0}'.format(i))
	plt.savefig('{0}'.format(i))
	plt.show()
	plt.close()

'''
scaler = MinMaxScaler()
scaler.fit(x_data)

scale_x_data = from_numpy(scaler.transform(x_data))

df = scale_x_data.numpy()

plt.hist(df.flatten(), bins=40, color='royalblue', alpha=0.7)
plt.xlim(0, 0.375)
plt.xlabel("MinMaxScale MET")
plt.savefig("MMS_met_pt")
plt.show()
'''
