import pandas as pd

filepath=r"C:\CNRL\BerlandDataFSCP.csv"

dat = pd.read_csv(filepath, sep=',', header=0)


dat= dat.sort_values(['UTM','Inspection Year'], ascending=[1,0])
print(dat.iloc[0:20,3:5])

dat_clean=dat.drop_duplicates(subset='UTM', keep='first')
print(dat_clean.iloc[0:20,3:5])
print(dat.size)
print(dat_clean.size)
#dat_clean.dropna(axis=0, how='all')

dat_clean=dat_clean.iloc[:,0:18]
dat_clean=dat_clean.dropna(subset=['UTM'])
#dat_clean= dat_clean.sort_values(['Location Id'], ascending=[1])
dat_clean['x'], dat_clean['y']=dat_clean['UTM'].str.split(' ',1).str
dat_clean.to_csv(r"C:\CNRL\BerlandDataFSCP_clean2.csv", sep=',', index=False)