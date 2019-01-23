
import os
import pandas as pd
import numpy as np


def culvert_road():
    return
def culvert_crossing():
    return
def culvert_creek():
    return


def culvert(dat):
    return dat

def main():
    path=r"C:\SCARI\\"
    csvname = "Scari_2016_postqc.csv"
    csvfile=path+csvname
    scarip = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)




if __name__ == "__main__":
    main()
