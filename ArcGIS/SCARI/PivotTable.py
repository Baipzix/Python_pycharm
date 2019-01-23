import pandas as pd
import numpy as np



##########
#read data

dids=pd.read_csv(filepath_or_buffer =r"C:\CNRL\GrandePrarie.txt", sep=",")

# pivot table sum
dids=dids[['COMPANY','CST','PoM','PoR']]
pd.pivot_table(dids,index=['COMPANY'], aggfunc='count')
roadtype=pd.pivot_table(dids,values='SHAPE_STLe',index=['NAME', 'Type'], aggfunc=np.sum)
#export to csv
did_t.to_csv(r"J:\2_Bonavista\DiDs_T.csv",sep=',', index=True)

#read again,

#transpose
did_t=Did1.pivot(index='NAME', columns='Type', values='SHAPE_STLe')
#export
did_t.to_csv(r"J:\2_Bonavista\DiDs_T.csv",sep=',', index=True)

##########






dids=pd.read_csv(filepath_or_buffer =r"C:\CNRL\GrandePrarie.txt", sep=",")

print(dids[0:10])
table=pd.pivot_table(dids,values='Perimeter',index=['COMPANY', 'Sections'])
company=dids[dids['COMPANY'].str.contains('ACCEL')]
print(company[0:10])
#tab_acc=pd.pivot_table(company, values='Perimeter', index='DISP_TYPE')
# print(table.sort_values(by=['Perimeter']))
#
# access=dids[dids['PURPCD'].str.contains('ACCESS')]
# print(access['PURPCD'])
#
# table=pd.pivot_table(access,values='Perimeter',index='COMPANY')
# print(table.sort_values(by=['Perimeter']))

table.to_csv(r"C:\ACCEL\201803\access_road_by_section.csv", sep=',', index=True)



#everything
table1=pd.pivot_table(dids,values='Perimeter',index=['Sections', 'COMPANY'], )
table.to_csv(r"C:\ACCEL\201803\access_road_by_section.csv", sep=',', index=True)
# road only

access=dids[dids['PURPCD'].str.contains('ACCESS')]
table2=pd.pivot_table(access,values='Perimeter',index=['Sections', 'COMPANY'])
table2.to_csv(r"C:\ACCEL\201803\road_section_company.csv", sep=',', index=True)




# HF

cutline=pd.read_csv(filepath_or_buffer =r"V:\Shared\Regulatory\TOLKO_DLO_APP\2018 analysis\cutline_section.txt", sep=",")
hf=pd.read_csv(filepath_or_buffer =r"V:\Shared\Regulatory\TOLKO_DLO_APP\2018 analysis\hf_section.txt", sep=",")
section=pd.read_csv(filepath_or_buffer =r"V:\Shared\Regulatory\TOLKO_DLO_APP\2018 analysis\ATS_SEC.txt", sep=",")

#pivot
clp=pd.pivot_table(cutline,values='Area',index=['DESCRIPTOR'], aggfunc=np.sum)
hfp=pd.pivot_table(hf,values='Area',index=['DESCRIPTOR'], aggfunc=np.sum)

#density

sc=section['DESCRIPTOR','SHAPE_Area']

sc_cl=pd.concat([sc,clp],axis=1)


#road
road=dids[dids['PURPCD'].str.contains("ACCESS")]
roadtype=pd.pivot_table(road,values='Perimeter',index=['COMPANY', 'DISP_TYPE'], aggfunc=np.sum)
roadcompany=pd.pivot_table(road,values='Perimeter',index=['COMPANY'], aggfunc=np.sum)
cnrl=dids[dids['COMPANY'].str.contains("CANADIAN NATURAL RESOURCES LIMITED")]


# csv file


did_t=Did1.pivot(index='NAME', columns='Type', values='SHAPE_STLe')


#

hf=pd.read_csv(filepath_or_buffer =r"J:\2_FRIAA\Gold Lake_Caribou\treatment\Regeneration.csv", sep=",")


