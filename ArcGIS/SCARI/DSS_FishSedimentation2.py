import pandas as pd
import numpy as np
import os
import sys


def erosion_score(ero, de, sed):


    ss = np.zeros(len(ero))

    ero[pd.isna(ero)]="No"

    ss[np.logical_and(ero == "No", sed == "No")] = 0
    ss[np.logical_and(ero == "No", sed == "Potential")] = 5
    ss[np.logical_and(ero == "No", sed == "Yes")] = 10

    ero_or = np.logical_or(ero == 'Potential', ero == 'Yes')

    ss[np.logical_and.reduce((ero_or, de == "Low", sed == "No"))] = 5
    ss[np.logical_and.reduce((ero_or, de == "Low", sed == "Potential"))] = 10
    ss[np.logical_and.reduce((ero_or, de == "Low", sed == "Yes"))] = 15

    ss[np.logical_and.reduce((ero_or, de == "High-unsatisfactory", sed == "No"))] = 10
    ss[np.logical_and.reduce((ero_or, de == "High-unsatisfactory", sed == "Potential"))] = 15
    ss[np.logical_and.reduce((ero_or, de == "High-unsatisfactory", sed == "Yes"))] = 20

    return ss


def outlet_score(outlet, block):
    ss = np.zeros(len(outlet))

    block[pd.isna(block)]="No"

    outlet=np.nan_to_num(outlet)

    ss[np.logical_and(outlet <= 0, block == "No")] = 0
    ss[np.logical_and(outlet <= 0, np.logical_or(block == "Potential", block == "Yes"))] = 5

    ss[np.logical_and(np.logical_and(outlet > 0, outlet < 10), block == "No")] = 15
    ss[np.logical_and(np.logical_and(outlet > 0, outlet < 10),
                      np.logical_or(block == "Potential", block == "Yes"))] = 20

    ss[np.logical_and(outlet >= 10, block == "No")] = 30
    ss[np.logical_and(outlet >= 10, np.logical_or(block == "Potential", block == "Yes"))] = 40
    return ss


def culvert_slope_score(slope):
    ss = np.zeros((len(slope)))

    #v1
    #ss[np.logical_or(slope == 'VERTICALLY BENT', slope == 'SLOPE > 2%')] = 10
    #v2 anything but Leve and uniform
    naslope=pd.isna(slope)
    ss[np.logical_and(slope != 'LEVEL AND UNIFORM', np.invert(naslope))] = 10
    return ss




def stream_score(stream):
    ss = np.zeros((len(stream)))
    ss[stream == 'INTERMITTENT'] = -10
    return ss

def risk_level(dat):

    #ss = np.zeros(dat.size)
    ss=np.empty(dat.size,dtype=np.chararray)
    ss[dat >=50] = 'High'
    ss[np.logical_and(dat >= 30, dat <=49)] = 'Moderate'
    ss[np.logical_and(dat >= 10, dat <= 29)] = 'Low'
    ss[dat<10] = 'No'
    return  ss



def dss_fish(dat):

    if "EROSION" not in dat.columns:
        sys.exit("EROSION doesn't exist")
    if "EROSION_DE" not in dat.columns:
        sys.exit("EROSION_DE doesn't exist")
    if "SEDEMENTAT" not in dat.columns:
        sys.exit("SEDEMENTAT doesn't exist")
    if "FISH_PCONC" not in dat.columns:
        sys.exit("FISH_PCONC doesn't exist")
    if "BLOCKAGE" not in dat.columns:
        sys.exit("BLOCKAGE doesn't exist")
    if "OUTLET_SCORE" not in dat.columns:
        sys.exit("OUTLET_SCORE doesn't exist")
    if "STR_CLASS" not in dat.columns:
        sys.exit("STR_CLASS doesn't exist")
    if "CULV_SLOPE" not in dat.columns:
        sys.exit("CULV_SLOPE doesn't exist")

    erosion = erosion_score(dat["EROSION"].values, dat["EROSION_DE"].values, dat["SEDEMENTAT"].values)
    outlet = outlet_score(dat["OUTLET_SCORE"].values, dat["BLOCKAGE"].values)

    str_class=dat["STR_CLASS"].str.upper()
    stream = stream_score(str_class.values)

    culv_slope=dat["CULV_SLOPE"].str.upper()
    slope = culvert_slope_score(culv_slope.values)
    # dat["erosion_score2"]=erosion
    # dat["outlet_score2"]=outlet
    # dat["stream_score2"]=stream
    # dat["slope_score2"]=slope
    sumpoint=erosion + outlet + stream + slope
    sumpoint[np.logical_or(dat["STR_CLASS"].values=="Ephemeral", dat["STR_CLASS"].values=="Cross Drain" )] =0
    dat["RISKFACTOR_Saft_Sedim_Outlet"] = sumpoint
    dat["Fish_Risk1"]=risk_level(dat["RISKFACTOR_Saft_Sedim_Outlet"].values)





def main():
    path=r"J:\2_SCARI\2018\\"
    csvname = "Scari_20180712_1.csv"
    outname="Scari_20180712_risk.csv"

    csvfile=path+csvname
    outputfile=path+outname

    if len(csvfile) == 0 or not os.path.exists(csvfile):
        csvfile = raw_input("Input file(CSV) name with full path: ")
    else:
        print("the file is: ", csvfile)
        inputname = raw_input(" Input \"Y\" to continue or Input file name with full path : ")
        if not (inputname != 'Y' or inputname != 'y'):
            csvfile = inputname

    while not os.path.exists(csvfile):
        csvfile = raw_input("Input the name again: ")

    print("Start to process data: ", csvfile)
    scarip = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)
    dss_fish(scarip)

    scarip.to_csv(outputfile, sep=',', index=False)


if __name__ == "__main__":
    main()
