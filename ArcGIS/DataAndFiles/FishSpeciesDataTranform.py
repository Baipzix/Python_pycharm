import pandas as pd
import numpy as np
import csv


def rawtodict(dat):
    # id=dat['GlobalID'].values
    # fish=dat['SPECIES_PR'].values
    newdat=dat[['GlobalID','SPECIES_PR']].copy()
    gid=['GlobalID']
    spr=['SPECIES_PR']

    for i in newdat.values:

        if ',' not in i[1]:
            spc_list=i[1]
            gid.append(i[0])
            spr.append(i[1])

        else:
            spltstring=map(str.strip, i[1].split(','))
            spc_list=spltstring
            spc_len=len(spc_list)

            gid.extend([i[0]]*spc_len)
            spr.extend(spc_list)

    d=np.column_stack((gid,spr))

    return d





def main():
    # file=r'J:\2_SCARI\2018\Scari_20180712_LSD.csv'
    file = r'J:\2_CNRL\SCARI_2018\FishModel\FishModelResult\fish_si.csv'
    outfile = r'J:\2_CNRL\SCARI_2018\FishModel\FishModelResult\fish_tsf.csv'
    scaridat = pd.read_csv(filepath_or_buffer=file, sep=',', header=0, low_memory=False)
    #print(scaridat[1:10])

    d=rawtodict(scaridat)

    with open(outfile, "wb") as f:
        writer=csv.writer(f)
        writer.writerows(d)



if __name__ == "__main__":
    main()
