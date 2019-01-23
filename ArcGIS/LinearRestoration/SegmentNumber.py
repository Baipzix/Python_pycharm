
import pandas as pd

def main():
    dat=r"J:\2_FRIAA\Gold Lake_Caribou\treatment\TreePlanting.csv"
    outputfile = r"J:\2_FRIAA\Gold Lake_Caribou\treatment\TreePlanting_sgmtNum.csv"
    line=pd.read_csv(dat)
    gline=line.sort_values(by=['LineName','x','y'], ascending=True).groupby('LineName')
    line['LineSegmen']=gline.cumcount()+1

    line.to_csv(outputfile, sep=',', index=False)


if __name__ == "__main__":
    main()