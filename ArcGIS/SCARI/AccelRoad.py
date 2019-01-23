import pandas as pd
import numpy as np

filepath=r"C:\ACCEL\201803\DiDs.txt"

dids=pd.read_csv(filepath)

road=dids[dids['PURPCD'].str.contains("ACCESS")]

table=pd.pivot_table(road,values='shp_len',index='COMPANY', aggfunc=np.sum)


#print(table.sort_values(by=['COMPANY']))

#table.to_csv(r"C:\ACCEL\201803\access_road.csv", sep=',', index=True)

accel=road[road['COMPANY'].str.contains("ACCEL")]

accel_table=pd.pivot_table(accel,values='shp_len',index=['COMPANY','Sections'], aggfunc=np.sum)
print(accel_table)
pen=road[road['COMPANY'].str.contains("PENGROWTH")]
pen_table=pd.pivot_table(pen,values='shp_len',index=['COMPANY','Sections'], aggfunc=np.sum)
print(pen_table)