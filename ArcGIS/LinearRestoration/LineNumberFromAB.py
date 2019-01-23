import pandas as pd
import math
import numpy as np
from string import ascii_uppercase



LETTERS={letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}

def ab_position(ch):
    #ch=ch.upper()
    number=[LETTERS[char] for char in ch if char in LETTERS]
    return number


def linenumber(str):
    strnum=ab_position(str)
    print(strnum)
    strlen=len(strnum)
    if strlen==1:
        return int(strnum[0])
    elif strlen>1 and not ('TL' in str):
        linen=0
        for n in range(strlen):
            num = int(strnum[n])
            pn = strlen - n - 1
            linen = linen + num * math.pow(26, pn)
        return int(linen)
    elif ('TL_' in str):
        if (strlen-2)==1:
            return int(strnum[2])+1000
        elif (strlen-2)>1:
            linen=1000
            for n in range(strlen-2):
                flag=n+2
                num=int(strnum[flag])
                pn=strlen-flag-1
                linen=linen+num*math.pow(26,pn)
            return int(linen)

def main():
    dat=r"J:\2_FRIAA\Gold Lake_Caribou\treatment\nametonumber.csv"
    outputfile=r"J:\2_FRIAA\Gold Lake_Caribou\treatment\nametonumber1.csv"
    line=pd.read_csv(dat)

    oid=line["OBJECTID"].values
    linename=line["Name"].values
    linenum=line["number"].values
    for id in oid:
        linenum[id]=linenumber(linename[id])
        #print(oid[id],'--------',linename[id],'------', linenum[id])
    line.to_csv(outputfile, sep=',', index=False)

if __name__ == "__main__":
    main()
