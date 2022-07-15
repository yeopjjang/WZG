import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

channel = ['eee','eem','emm','mmm']

def draw(channel):

	infile = "/x6/spool/dylee/workspace/aQGC/test_ML/data/"+channel+"_binary.h5"
	df = pd.read_hdf(infile)
	
	df_cor = df.iloc[:, 3:-6].corr()
	
	print(df_cor)

	sns.clustermap(df_cor, cmap = 'RdYlBu_r', linewidth=.5, vmin=-1, vmax=1)	
	plt.savefig("{0}_cor.png".format(channel))
	plt.close

	return df_cor

draw(channel[0])

