import pandas as pd


#filepath=r"C:\SCARI\Scari_DSS_2017_geoff.xlsx"
filepath=r'C:\\SCARI\\Fullsize\\Scari_2016_postqc.xlsx'

scari=pd.read_excel(filepath)
dss=scari[['ID','EROSION','SEDEMENTAT','EROSION_DE','OUTLET_SCORE','BLOCKAGE','CULV_SLOPE','STR_CLASS']]

print(len(colname))
print(colname[0:10])
print(colname[10:20])
print(colname[20:30])
print(colname[30:40])
print(colname[40:50])
print(colname[50:60])
print(colname[60:70])
print(colname[70:80])
print(colname[80:90])
print(colname[90:100])
print(colname[100:110])
print(colname[110:120])
print(colname[120:130])
print(colname[130:134])


print(dss.iloc[[1386]])



filepath=r"C:\CNRL\GrandePrarie.txt"
grande=pd.read_csv(filepath)
print(grand)