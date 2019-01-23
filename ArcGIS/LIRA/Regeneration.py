
import os
import pandas as pd
import numpy as np

def reg_model(sd, avg):
    tmp=np.empty(sd.size, dtype=np.chararray)

    # high
    #sd_level= np.logical_or(sd == 'L', sd == 'M')
    #tmp[np.logical_and(avg=='H', sd_level )] = 'H'


    tmp[np.logical_and(avg>=2, sd<=2 )] = 'H'

    # medium
    # tmp[np.logical_and(avg == 'H', sd == 'M')] = 'M'
    # sd_level = np.logical_or(sd == 'L', sd == 'M')
    # tmp[np.logical_and(avg == 'M', sd_level)] = 'M'

    #tmp[np.logical_and(avg == 'H', sd == 'H')] = 'M'
    tmp[np.logical_and(avg >=2, sd == 3)] = 'M'

    # low
    #tmp[np.logical_and(avg == 'M', sd=='H')] = 'L'
    tmp[avg==1]='L'

    return tmp




def main():
    path=r"J:\2_FRIAA\Gold Lake_Caribou\treatment\\"
    csvname = "TreatmentCNHTDWEC.csv"
    outname="TreatmentCNHTDWEC_Reg.csv"


    csvfile=path+csvname
    outputfile=path+outname


    avi = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)
    sd=avi['Canopy'].values
    avg=avi['Height'].values
    avi['reg']=reg_model(sd, avg)
    #df_reg=avi[['OBJECTID','reg']]
    avi.to_csv(outputfile, sep=',', index=False)


if __name__ == "__main__":
    main()
