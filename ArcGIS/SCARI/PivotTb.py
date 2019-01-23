import pandas as pd
import numpy as np


dfile=r"J:\2_FRIAA\Gold Lake_Caribou\data\Risk\crossing_dtw_cln.csv"

dt=pd.read_csv(filepath_or_buffer =dfile, sep=",", low_memory=False)

table=pd.pivot_table(dt,values='Area',index=['Crossing','dtw'],aggfunc='sum')




table=dt.groupby(['Crossing','dtw'])['Area'].sum()/dt.groupby(['Crossing'])['Area'].sum()


#print(table)

# for tb in table['crossing']:
#     print(tb)
#     print("----------")

#table.to_csv(r"J:\2_FRIAA\Gold Lake_Caribou\data\Risk\crossing_dtw_tab.csv", sep=',')

dft=pd.DataFrame(table, columns=['crossing','dtw','rate'])
print(dft)