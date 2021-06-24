import numpy as np
import pandas as pd

infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/testML/data/binary.h5"

df = pd.read_hdf(infile)

print(df)
print(df.columns)
