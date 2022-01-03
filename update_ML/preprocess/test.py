import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Load
eee_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/splitML/preprocess/eee_binary.h5"
eem_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/splitML/preprocess/eem_binary.h5" 
emm_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/splitML/preprocess/emm_binary.h5"
mmm_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/splitML/preprocess/mmm_binary.h5"

eee_df = pd.read_hdf(eee_infile)
eem_df = pd.read_hdf(eem_infile)
emm_df = pd.read_hdf(emm_infile)
mmm_df = pd.read_hdf(mmm_infile)

print(eee_df.columns)

'''
# Add necessary columns
eee_df['weight'] = (eee_df['xsec'] * 3000000)/eee_df['Event']
eem_df['weight'] = (eem_df['xsec'] * 3000000)/eem_df['Event']
emm_df['weight'] = (emm_df['xsec'] * 3000000)/emm_df['Event']
mmm_df['weight'] = (mmm_df['xsec'] * 3000000)/mmm_df['Event']

eee_sigY = eee_df[eee_df['y'] == 1]['weight'].sum(axis = 0, skipna = False)
eem_sigY = eem_df[eem_df['y'] == 1]['weight'].sum(axis = 0, skipna = False)
emm_sigY = emm_df[emm_df['y'] == 1]['weight'].sum(axis = 0, skipna = False)
mmm_sigY = mmm_df[mmm_df['y'] == 1]['weight'].sum(axis = 0, skipna = False)

eee_bkgY = eee_df[eee_df['y'] == 0]['weight'].sum(axis = 0, skipna = False)
eem_bkgY = eem_df[eem_df['y'] == 0]['weight'].sum(axis = 0, skipna = False)
emm_bkgY = emm_df[emm_df['y'] == 0]['weight'].sum(axis = 0, skipna = False)
mmm_bkgY = mmm_df[mmm_df['y'] == 0]['weight'].sum(axis = 0, skipna = False)

eee_sf = eee_sigY/eee_bkgY
eem_sf = eem_sigY/eem_bkgY
emm_sf = emm_sigY/emm_bkgY
mmm_sf = mmm_sigY/mmm_bkgY

eee_data, eem_data, emm_data, mmm_data = [],[],[],[]

for i in eee_df['y']:
        if i == 1:
                eee_data.append(1)
        else:
                eee_data.append(eee_sf)

for i in eem_df['y']:
        if i == 1:
                eem_data.append(1)
        else:
                eem_data.append(eem_sf)

for i in emm_df['y']:
        if i == 1:
                emm_data.append(1)
        else:
                emm_data.append(emm_sf)

for i in mmm_df['y']:
        if i == 1:
                mmm_data.append(1)
        else:
                mmm_data.append(mmm_sf)

eee_df['SF'] = eee_data
eem_df['SF'] = eem_data
emm_df['SF'] = emm_data
mmm_df['SF'] = mmm_data

# Redefine lep3 F, C
eee_df['lep3_Flav'] = eee_df['lep3_C'] * (eee_df['lep3_F'] + 1)
eem_df['lep3_Flav'] = eem_df['lep3_C'] * (eem_df['lep3_F'] + 1)
emm_df['lep3_Flav'] = emm_df['lep3_C'] * (emm_df['lep3_F'] + 1)
mmm_df['lep3_Flav'] = mmm_df['lep3_C'] * (mmm_df['lep3_F'] + 1)

eee_signal_N = len(eee_df['weight'][eee_df['y'] == 1])
eem_signal_N = len(eem_df['weight'][eem_df['y'] == 1])
emm_signal_N = len(emm_df['weight'][emm_df['y'] == 1])
mmm_signal_N = len(mmm_df['weight'][mmm_df['y'] == 1])

eee_bkg_N = eee_df['weight'][eee_df['y'] == 0].sum()
eem_bkg_N = eem_df['weight'][eem_df['y'] == 0].sum()
emm_bkg_N = emm_df['weight'][emm_df['y'] == 0].sum()
mmm_bkg_N = mmm_df['weight'][mmm_df['y'] == 0].sum()

eee_SF = eee_signal_N / eee_bkg_N
eem_SF = eem_signal_N / eem_bkg_N
emm_SF = emm_signal_N / emm_bkg_N
mmm_SF = mmm_signal_N / mmm_bkg_N

print("eee signal : {0}, bkg : {1}, SF : {2}".format(eee_signal_N, eee_bkg_N, eee_SF))
print("eem signal : {0}, bkg : {1}, SF : {2}".format(eem_signal_N, eem_bkg_N, eem_SF))
print("emm signal : {0}, bkg : {1}, SF : {2}".format(emm_signal_N, emm_bkg_N, emm_SF))
print("mmm signal : {0}, bkg : {1}, SF : {2}".format(mmm_signal_N, mmm_bkg_N, mmm_SF))

eee_df['weight'][eee_df['y'] == 1] = 1
eem_df['weight'][eem_df['y'] == 1] = 1
emm_df['weight'][emm_df['y'] == 1] = 1
mmm_df['weight'][mmm_df['y'] == 1] = 1

eee_df['weight'][eee_df['y'] == 0] = eee_df['weight'][eee_df['y'] == 0] * eee_SF
eem_df['weight'][eem_df['y'] == 0] = eem_df['weight'][eem_df['y'] == 0] * eem_SF
emm_df['weight'][emm_df['y'] == 0] = emm_df['weight'][emm_df['y'] == 0] * emm_SF
mmm_df['weight'][mmm_df['y'] == 0] = mmm_df['weight'][mmm_df['y'] == 0] * mmm_SF

eee_df_weight = eee_df['weight']
eem_df_weight = eem_df['weight']
emm_df_weight = emm_df['weight']
mmm_df_weight = mmm_df['weight']

eee_df = eee_df.drop(['weight', 'SF'], axis=1)
eem_df = eem_df.drop(['weight', 'SF'], axis=1)
emm_df = emm_df.drop(['weight', 'SF'], axis=1)
mmm_df = mmm_df.drop(['weight', 'SF'], axis=1)

eee_df['weight'] = eee_df_weight
eem_df['weight'] = eem_df_weight
emm_df['weight'] = emm_df_weight
mmm_df['weight'] = mmm_df_weight


# Remove unnecessary columns
eee_df = eee_df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass', 'Pho_E', 'lep1_E', 'lep2_E', 'lep3_E', 'lep1_F', 'lep1_C', 'lep2_F', 'lep2_C', 'lep3_C', 'lep3_F', 'lep2_eta'], axis=1)
eem_df = eem_df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass', 'Pho_E', 'lep1_E', 'lep2_E', 'lep3_E', 'lep1_F', 'lep1_C', 'lep2_F', 'lep2_C', 'lep3_C', 'lep3_F', 'lep2_eta'], axis=1)
emm_df = emm_df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass', 'Pho_E', 'lep1_E', 'lep2_E', 'lep3_E', 'lep1_F', 'lep1_C', 'lep2_F', 'lep2_C', 'lep3_C', 'lep3_F', 'lep2_eta'], axis=1)
mmm_df = mmm_df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass', 'Pho_E', 'lep1_E', 'lep2_E', 'lep3_E', 'lep1_F', 'lep1_C', 'lep2_F', 'lep2_C', 'lep3_C', 'lep3_F', 'lep2_eta'], axis=1)

print(eee_df)
print(eem_df)
print(emm_df)
print(mmm_df)

eee_df.to_hdf('eee_binary.h5', key = 'df', mode = 'w')
eem_df.to_hdf('eem_binary.h5', key = 'df', mode = 'w')
emm_df.to_hdf('emm_binary.h5', key = 'df', mode = 'w')
mmm_df.to_hdf('mmm_binary.h5', key = 'df', mode = 'w')

'''
