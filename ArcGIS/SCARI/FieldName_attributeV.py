
import os
import pandas as pd
import numpy as np


def listname(dat):
    colnames=list(dat)
    fieldNum=len(colnames)
    if fieldNum >10:
        i0=0
        for i in xrange(0,fieldNum,10):
            i1=i0+10
            print(colnames[i0:i1])
            i0=i1
    else:
        print(colnames)

def uniqueV(dat):
    if len(dat)>1:

    else:
        namelist=pd.unique(dat)
    listname(namelist)

def main():
    path=r"C:\SCARI\\"
    csvname = "Scari_2016_postqc.csv"
    csvfile=path+csvname
    scarip = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)
    listname(scarip)



if __name__ == "__main__":
    main()
