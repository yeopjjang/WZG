import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_file = "../run/history.csv"
history_df = pd.read_csv(csv_file)

history_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.savefig('loss')

plt.close()
history_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.savefig('acc')
