import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn

# Data Load
infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"
df = pd.read_hdf(infile)

# use pandas 
df_shuffled_pd = df.sample(frac=1).reset_index(drop=True)

# use numpy 
df_shuffled_np = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)

# use sklearn
df_shuffled_sk = sklearn.utils.shuffle(df)


df_shuffled_sk.to_hdf('binary.h5', key = 'df', mode = 'w')

