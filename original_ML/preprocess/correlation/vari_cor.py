import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/data/mixbinary.h5"
df = pd.read_hdf(infile)

df_cor = df.iloc[:, 3:-1].corr()

sns.clustermap(df_cor, cmap = 'RdYlBu_r', linewidths=.5, vmin=-1, vmax=1)


#f, ax = plt.subplots(figsize=(11,9))

#cmap = sns.diverging_palette(230, 20, as_cmap=True)

#sns.heatmap(corr, cmap=cmap, vmax=1, center=0, square=False, linewidths=.5, cbar_kws={"shrink": .5})
plt.savefig("mix_cor.png")
plt.show()
