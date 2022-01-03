import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

eee_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/low_ML/data/eee_binary.h5"
eem_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/low_ML/data/eem_binary.h5"
emm_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/low_ML/data/emm_binary.h5"
mmm_infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/low_ML/data/mmm_binary.h5"

eee_df = pd.read_hdf(eee_infile)
eem_df = pd.read_hdf(eem_infile)
emm_df = pd.read_hdf(emm_infile)
mmm_df = pd.read_hdf(mmm_infile)

eee_df_cor = eee_df.iloc[:, 3:-2].corr()
eem_df_cor = eem_df.iloc[:, 3:-2].corr()
emm_df_cor = emm_df.iloc[:, 3:-2].corr()
mmm_df_cor = mmm_df.iloc[:, 3:-2].corr()

sns.clustermap(eee_df_cor, cmap = 'RdYlBu_r', linewidths=.5, vmin=-1, vmax=1)
plt.savefig("eee_cor.png")
plt.close()

sns.clustermap(eem_df_cor, cmap = 'RdYlBu_r', linewidths=.5, vmin=-1, vmax=1)
plt.savefig("eem_cor.png")
plt.close()

sns.clustermap(emm_df_cor, cmap = 'RdYlBu_r', linewidths=.5, vmin=-1, vmax=1)
plt.savefig("emm_cor.png")
plt.close()

sns.clustermap(mmm_df_cor, cmap = 'RdYlBu_r', linewidths=.5, vmin=-1, vmax=1)
plt.savefig("mmm_cor.png")
plt.close()



