import pandas as pd
import numpy as np
import os

df = pd.read_csv('rf.csv')
#df2 = df1[slice of df1 goes here]
df1 = df[df['Instructor Last Name'].notna
#we want to remove rows containing a value of NaN in the 'Instructor Last Name' field
df1.to_csv('rf2.csv')
