import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Load
infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"
df = pd.read_hdf(infile)


# Remove unnecessary columns
df = df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass'], axis=1)


# Add necessary columns
df['weight'] = (df['xsec'] * 3000000)/df['Event']

sigY = df[df['y'] == 0]['weight'].sum(axis = 0, skipna = False)

bkgY = df[df['y'] == 1]['weight'].sum(axis = 0, skipna = False)

sf = sigY/bkgY

data = []

for i in df['y']:
	if i == 0:
		data.append(1)
	else:
		data.append(sf)

df['SF'] = data

df.to_hdf('binary.h5', key = 'df', mode = 'w')

