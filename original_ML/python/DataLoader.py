import torch
from torch import from_numpy
from torch.utils.data import Dataset
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import sklearn

## Read ntuple
#infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/data/binary.h5"
infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/data/highbinary.h5"

df = pd.read_hdf(infile)

#df_shuffled_sk = sklearn.utils.shuffle(df)

## Split data
train_df, val_df, test_df = np.split(df.sample(frac=1, random_state=42),
					[int(.6*len(df)), int(.8*len(df))])
# Train data
train_x = train_df.iloc[:, 3:-1].values
train_y = train_df.iloc[:,[0]].values 
train_w = train_df.iloc[:, [-1]].values

# Validation data
val_x = val_df.iloc[:, 3:-1].values 
val_y = val_df.iloc[:,[0]].values 
val_w = val_df.iloc[:, [-1]].values

# Test data
test_x = test_df.iloc[:, 3:-1].values 
test_y = test_df.iloc[:,[0]].values 
test_w = test_df.iloc[:, [-1]].values


## Standardization & Normalization
STD_scaler = StandardScaler()
STD_scaler.fit(train_x)

Base_scaler = MinMaxScaler()
Base_scaler.fit(train_x)

train_x = STD_scaler.transform(train_x)
val_x = STD_scaler.transform(val_x)
test_x = STD_scaler.transform(test_x)


# Dataset class
class TrainDataset(Dataset):
	
	def __init__(self):

		self.train_x = from_numpy(train_x)
		self.train_y = from_numpy(train_y)
		self.train_w = from_numpy(train_w)

	def __getitem__(self, index):
		return self.train_x[index], self.train_y[index], self.train_w[index]

	def __len__(self):
		self.len = len(train_df)
		return self.len


class ValDataset(Dataset):

	def __init__(self):

		self.val_x = from_numpy(val_x)
		self.val_y = from_numpy(val_y)
		self.val_w = from_numpy(val_w)

	def __getitem__(self, index):
		return self.val_x[index], self.val_y[index], self.val_w[index]

	def __len__(self):
		self.len = len(val_df)
		return self.len

class TestDataset(Dataset):

	def __init__(self):

		self.test_x = from_numpy(test_x)
		self.test_y = from_numpy(test_y)
		self.test_w = from_numpy(test_w)

	def __getitem__(self, index):
		return self.test_x[index], self.test_y[index], self.test_w[index]

	def __len__(self):
		self.len = len(test_df)
		return self.len

