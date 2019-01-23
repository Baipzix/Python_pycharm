import numpy as np
import pandas as pd



# read the csv
filepath=r""
ppoint=pd.read_csv(filepath, sep=',', header=0)


group = ppoint.groupby('x','y')['Name'].unique()