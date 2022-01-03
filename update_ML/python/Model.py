import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

	def __init__(self):
		super(Model, self).__init__()

		self.fc = nn.Sequential(

			# 1st layer
			nn.Linear(16, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),
			
			# 2nd layer
            		nn.Linear(1024, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),
			
			# 3rd layer
            		nn.Linear(1024, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),

			# 4th layer
			nn.Linear(1024, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),

			# 5th layer
            		nn.Linear(1024, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),

			# 6th layer
			nn.Linear(1024, 1024),
			nn.ReLU(),
			nn.BatchNorm1d(1024),
			nn.Dropout(0.5),
		
			# 7th layer
			nn.Linear(1024,64),
			nn.ReLU(),
			nn.BatchNorm1d(64),

			# 8th layer
            		nn.Linear(64, 1),
			nn.Sigmoid(),
		)


	def forward(self, x):
		y_pred = self.fc(x)
		return y_pred
