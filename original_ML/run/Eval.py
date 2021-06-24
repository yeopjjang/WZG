import numpy as np
import pandas as pd
import sys, os
import matplotlib.pyplot as plt

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


sys.path.append("../python")
from DataLoader import TestDataset

test_dataset = TestDataset()

test_loader = DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False,num_workers=2)


## Device set and Optimizer set
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
        model = Model()
        model = model.to('cuda')
        device = 'cuda'

model.load_state_dict(torch.load('weightFile.pth'))

optm = optim.Adam(model.parameters(), lr=LR)


# Evaluation
from tqdm.auto import tqdm
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

labels, preds = [], []
weights, scaleWeights = [], []
predFile = 'prediction.csv'

for i, (test_x, label, weight) in enumerate(tqdm(test_loader)):
	test_x = test_x.float().to(device)
	weight = weight.float()
	pred = model(test_x).detach().to('cpu').float()

	labels.extend([x.item() for x in label])
	preds.extend([x.item() for x in pred.view(-1)])
	weights.extend([x.item() for x in weight.view(-1)]) 

df = pd.DataFrame({'label': labels, 'prediction': preds, 'weight': weights})
df.to_csv(predFile, index=False)
