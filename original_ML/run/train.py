import numpy as np
import pandas as pd
import sys, os
import csv

import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn, from_numpy, optim
from torch.utils.data.dataset import random_split
import torch.nn.functional as F

## Check GPU
def GPU_check():
	if torch.cuda.is_available():

		nGPU = torch.cuda.device_count()
		print("Number of GPU : {0}".format(nGPU))
	
		for i,j in enumerate(range(nGPU)):
			print("Device", i, torch.cuda.get_device_name(i))

	else:
		print("No GPU for use")

GPU_check()
use_gpu=True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--epoch', type=int,default=200,
            help="--epoch EPOCH")
parser.add_argument('--batch', type=int,default=4096,
            help="--batch BATCH_SIZE")
parser.add_argument('--lr', type=float,default=0.01,
            help="--lr LEARNING_RATE")
args = parser.parse_args()

## Hyperparameter
batch_size = args.batch
LR = args.lr
EPOCH = args.epoch


##  Data load
sys.path.append("../python/")
from DataLoader import TrainDataset, ValDataset

train_dataset = TrainDataset()
val_dataset = ValDataset()

train_loader = DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=False,num_workers=2)
val_loader = DataLoader(dataset=val_dataset,batch_size=batch_size*2,shuffle=False,num_workers=2)


## Model load
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
	model = Model()
	model = model.to('cuda')
	device = 'cuda'

optm = optim.Adam(model.parameters(), lr=LR)


## Training with GPU
from tqdm.auto import tqdm
from sklearn.metrics import accuracy_score

bestWeight, bestLoss = {}, 1e9
try:
	history = {'train_loss': [], 'train_accuracy': [], 'val_loss': [], 'val_accuracy': []}

# Start EPOCH
	for epoch in tqdm(range(1,EPOCH+1)):

		# Training Stage
		model.train()
		optm.zero_grad() # initialize grad data
		train_loss, train_acc = 0., 0.
		
		for i, (train_x, label, train_w) in enumerate(train_loader):
			
			train_x = train_x.float().to(device) # Make tensor on the gpu or cpu
			label = label.float().to(device)
			weight = train_w.float().to(device)
			
			pred = model(train_x)
			crit = torch.nn.BCELoss(weight=weight) # binary cross entropy
		
			if device == 'cuda': crit = crit.cuda() # GPU case
			loss = crit(pred,label)
			loss.backward()

			optm.step()

			train_loss += loss.item()
			train_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0), sample_weight=weight.view(-1).to('cpu'))
		
		train_loss /= len(train_loader)
		train_acc /= len(train_loader)

		# Validation Stage
		model.eval()
		val_loss, val_acc = 0., 0.
		
		for i, (val_x, label, val_w) in enumerate(val_loader):
			val_x = val_x.float().to(device)
			label = label.float().to(device)
			weight = val_w.float().to(device)	
	
			pred = model(val_x)
			crit = torch.nn.BCELoss(weight=weight)

			loss = crit(pred,label)
			val_loss += loss.item()
			val_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0), sample_weight=weight.view(-1).to('cpu'))

		val_loss /= len(val_loader)
		val_acc /= len(val_loader)

		# Update weight of best epoch checking validation loss
		if bestLoss > val_loss:
			bestWeight = model.state_dict()
			bsetLoss = val_loss
			
			torch.save(bestWeight, 'weightFile.pth')		

		history['train_loss'].append(train_loss)
		history['train_accuracy'].append(train_acc)
		history['val_loss'].append(val_loss)
		history['val_accuracy'].append(val_acc)

		if epoch % 10 == 1:
			print("Epoch: {0}, Train Loss: {1}, Val Loss: {2}, Train Acc: {3}, Val Acc: {4}".format(epoch,train_loss,val_loss,train_acc,val_acc))

		with open('history.csv', 'w') as f:
			writer = csv.writer(f)
			keys = history.keys()
			writer.writerow(keys)
			for row in zip(*[history[key] for key in keys]):
				writer.writerow(row)
		

except KeyboardInterrupt:
	print("Muyaho!")

