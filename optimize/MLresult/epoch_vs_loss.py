import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

## Read csv
eee_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/less/eee/history.csv'
eem_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/512neuron/more/eem/history.csv'
emm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/1024neuron/most/emm/history.csv'
mmm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/fixver_ML/Storage/4096neuron/much/mmm/history.csv'

eee_df = pd.read_csv(eee_infile)
eem_df = pd.read_csv(eem_infile)
emm_df = pd.read_csv(emm_infile)
mmm_df = pd.read_csv(mmm_infile)

eee_df[['Train Loss', 'Validation Loss', 'Train Accuracy', 'Validation Accuracy']] = eee_df[['train_loss', 'val_loss', 'train_accuracy', 'val_accuracy']]
eem_df[['Train Loss', 'Validation Loss', 'Train Accuracy', 'Validation Accuracy']] = eem_df[['train_loss', 'val_loss', 'train_accuracy', 'val_accuracy']]
emm_df[['Train Loss', 'Validation Loss', 'Train Accuracy', 'Validation Accuracy']] = emm_df[['train_loss', 'val_loss', 'train_accuracy', 'val_accuracy']]
mmm_df[['Train Loss', 'Validation Loss', 'Train Accuracy', 'Validation Accuracy']] = mmm_df[['train_loss', 'val_loss', 'train_accuracy', 'val_accuracy']]

## Draw acc and loss

# eee channel
plt.style.use(hep.style.CMS)
eee_df[['Train Loss', 'Validation Loss']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Loss",fontsize=20,loc='center')
plt.text(5,24, '(eee channel)', fontsize=25)
plt.legend(fontsize=20, loc='upper right')
plt.savefig('eee_loss')
plt.show()
plt.close()

plt.style.use(hep.style.CMS)
eee_df[['Train Accuracy', 'Validation Accuracy']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Accuracy",fontsize=20,loc='center')
plt.text(5, 0.78, '(eee channel)', fontsize=25)
plt.legend(fontsize=20, loc='lower right')
plt.savefig('eee_acc')
plt.show()
plt.close()


# eem channel
plt.style.use(hep.style.CMS)
eem_df[['Train Loss', 'Validation Loss']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Loss",fontsize=20,loc='center')
plt.text(130,9, '(ee$\mu$ channel)', fontsize=25)
plt.legend(fontsize=20, loc='upper right')
plt.savefig('eem_loss')
plt.show()
plt.close()

plt.style.use(hep.style.CMS)
eem_df[['Train Accuracy', 'Validation Accuracy']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Accuracy",fontsize=20,loc='center')
plt.text(5, 0.78, '(ee$\mu$ channel)',fontsize=25)
plt.legend(fontsize=20, loc='lower right')
plt.savefig('eem_acc')
plt.show()
plt.close()


# emm channel
plt.style.use(hep.style.CMS)
emm_df[['Train Loss', 'Validation Loss']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Loss",fontsize=20,loc='center')
plt.text(10, 45, '(e$\mu\mu$ channel)', fontsize=25)
plt.legend(fontsize=20, loc='upper right')
plt.savefig('emm_loss')
plt.show()
plt.close()

plt.style.use(hep.style.CMS)
emm_df[['Train Accuracy', 'Validation Accuracy']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Accuracy",fontsize=20,loc='center')
plt.text(90, 0.48, '(e$\mu\mu$ channel)', fontsize=25)
plt.legend(fontsize=20, loc='upper left')
plt.savefig('emm_acc')
plt.show()
plt.close()

# mmm channel
plt.style.use(hep.style.CMS)
mmm_df[['Train Loss', 'Validation Loss']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Loss",fontsize=20,loc='center')
plt.text(130, 50, '($\mu\mu\mu$ channel)',fontsize=25)
plt.legend(fontsize=20, loc='upper right')
plt.savefig('mmm_loss')
plt.show()
plt.close()

plt.style.use(hep.style.CMS)
mmm_df[['Train Accuracy', 'Validation Accuracy']].plot()
plt.xlabel("Epoch",fontsize=20,loc='center')
plt.ylabel("Accuracy",fontsize=20,loc='center')
plt.text(5, 0.77, '($\mu\mu\mu$ channel)',fontsize=25)
plt.legend(fontsize=20, loc='lower right')
plt.savefig('mmm_acc')
plt.show()
plt.close()


