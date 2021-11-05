import pandas as pd
import numpy as np
import os

df1 = pd.read_csv('rf.csv')
#df2 = df1[slice of df1 goes here]

#we want to remove rows containing a value of NaN in the 'Instructor Last Name' field
for label in df2['Instructor Last Name']:
    print(label)
