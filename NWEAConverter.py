import pandas as pd
import numpy as np
import os

df = pd.read_csv('rf.csv')
#we want to remove rows containing a value of NaN in the 'Instructor Last Name' field
df1 = df[df['Instructor Last Name'].notna()]

#Creating a new file, "rf2.csv" so we can compare with original file, will squash original file in final product
df1.to_csv('rf2.csv')
