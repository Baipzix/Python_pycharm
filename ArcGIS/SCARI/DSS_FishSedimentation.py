import pandas as pd
import numpy as np
import os
import sys


def erosion_score(ero, de, sed):
    ss = np.zeros(len(ero))

    ss[np.logical_and(ero == "No", sed == "No")] = 0
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "Low", sed == "No")] = 5
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory", sed == "No")] = 10

    ss[np.logical_and(ero == "No", sed == "Potential")] = 5
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "Low", sed == "Potential")] = 10
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory",
                      sed == "Potential")] = 15

    ss[np.logical_and(ero == "No", sed == "Yes")] = 10
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "Low", sed == "Yes")] = 15
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory", sed == "Yes")] = 20
    return ss


def fish_score(fish, block):
    fs = np.zeros(len(fish))

    fs[np.logical_and(fish == "No Concerns", block == "No")] = 0
    fs[np.logical_and(fish == "No Concerns", np.logical_or(block == 'Potential', block == 'Yes'))] = 5

    fs[np.logical_and(fish == "Some Concerns", block == "No")] = 15
    fs[np.logical_and(fish == "Some Concerns", np.logical_or(block == 'Potential', block == 'Yes'))] = 20

    fs[np.logical_and(fish == "Serious Concerns", block == "No")] = 30
    fs[np.logical_and(fish == "Serious Concerns", np.logical_or(block == 'Potential', block == 'Yes'))] = 40

    return fs


def dss_fish(dat):
    sLen = len(dat.index)
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

    erosion = erosion_score(dat["EROSION"].values, dat["EROSION_DE"].values, dat["SEDEMENTAT"].values)
    fish = fish_score(dat["FISH_PCONC"].values, dat["BLOCKAGE"].values)
    dat["RISKFACTOR_fish"] = erosion + fish


def main():
    csvfile = r"C:\SCARI\ScariData.csv"

    if len(csvfile) == 0 or not os.path.exists(csvfile):
        csvfile = raw_input("Input file(CSV) name with full path: ")
    else:
        print("the file is: ", csvfile)
        inputname = raw_input(" Input \"Y\" to continue or Input file name with full path : ")
        if not(inputname!='Y' or inputname!='y'):
            csvfile=inputname

    while not os.path.exists(csvfile):
        csvfile = raw_input("Input the name again: ")

    print("Start to process data: ", csvfile)
    scarip = pd.read_csv(csvfile, sep=',', header=0)
    dss_fish(scarip)

    scarip.to_csv(r"C:\SCARI\ScariOut2.csv", sep=',', index=False)


if __name__ == "__main__":
    main()
