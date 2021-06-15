import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"
df = pd.read_hdf(infile)

df_cor = df.iloc[:, 3:]

corr = df_cor.corr()

f, ax = plt.subplots(figsize=(11,9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(corr, cmap=cmap, vmax=1, center=0, square=False, linewidths=.5, cbar_kws={"shrink": .5})
plt.savefig("correlation.png")
plt.show()
