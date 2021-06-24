import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Load
infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/preprocess/binary.h5"
df = pd.read_hdf(infile)


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
print(df['SF'])

'''
# Redefine lep3 F, C
df['lep3_Flav'] = df['lep3_C'] * (df['lep3_F'] + 1)
'''
signal_N = len(df['weight'][df['y']==0])
bkg_N = df['weight'][df['y']==1].sum()

SF = signal_N / bkg_N

print(signal_N, bkg_N, SF)


df['weight'][df['y']==0] = 1
df['weight'][df['y']==1] = df['weight'][df['y']==1] * SF
df_weight = df['weight']

df = df.drop(['SF', 'weight'], axis=1)

df['weight'] = df_weight

print(df['weight'])

'''
# Remove unnecessary columns
df = df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass', 'Pho_E', 'lep1_E', 'lep2_E', 'lep3_E', 'lep1_F', 'lep1_C', 'lep2_F', 'lep2_C', 'lep3_C', 'lep3_F'], axis=1)
'''
print(df)
print(df.columns)
df.to_hdf('binary.h5', key = 'df', mode = 'w')

