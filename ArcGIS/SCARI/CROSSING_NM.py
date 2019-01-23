# give each crossing a CROSS_NM
# name structure is:


import pandas as pd
import numpy as np

def LSD_group(dat):
    lsd_ls = int(dat['LS'].values[0])
    lsd_sec = int(dat['SEC'].values[0])
    lsd_twp = int(dat['TWP'].values[0])
    lsd_rge = int(dat['RGE'].values[0])
    lsd_m = int(dat['M'].values[0])
    crossNm = dat['CROSS_NM'].values
    totalNm = crossNm.size

    snumber = []

    for idx in range(totalNm):

        if pd.notna(crossNm[idx]) and len(crossNm[idx])>15:
            tm = crossNm[idx][-2:-1]
            snumber.append(int(tm))

    if len(snumber):
        i = max(snumber) + 1
    else:
        i = 1

    for idx in range(totalNm):
        if pd.isna(crossNm[idx]) or len(crossNm[idx])<= 15:
            try:
                crossNm[idx] = 'WCX ' + str(lsd_ls) + '-' + str(lsd_sec) + '-' + str(lsd_twp) + '-' + \
                               str(lsd_rge) + ' W' + str(lsd_m) + ' (' + str(i) + ')'
                i = i + 1
            except ValueError, e:
                print("error", e, "on the row: ",crossNm[idx])
    return crossNm


def crossing_nm(dat):
    colNm = 'DESCRIPTOR'

    ss = np.empty(len(dat[colNm]), dtype='S50')
    lsd = list(set(dat[colNm].values))

    s_lsd=pd.Series(lsd)
    s_lsd=s_lsd.dropna()
    s_lsd=s_lsd.str.replace('RA ','')

    for twn in s_lsd:
        # sub_lsd = dat[dat[colNm].values==twn]
        # print(sub_lsd)
        # print('----=twn -----')
        sub_lsd=dat[dat[colNm].str.contains(twn)==True]
        ss[dat[colNm].str.contains(twn)==True] = LSD_group(sub_lsd)

    dat['CROSS_NM']=ss

    return dat


def main():

    file = r'J:\2_SCARI\2018\CrossingName_Oct19\SCARI_latlong_LSD.csv'
    outfile = r'J:\2_SCARI\2018\CrossingName_Oct19\SCARI_LSD_Name.csv'
    scaridat = pd.read_csv(filepath_or_buffer=file, sep=',', header=0, low_memory=False) #lineterminator='\n')

    if 'CROSS_NM' not in scaridat.columns:
        slength=len(scaridat.index)
        scaridat['CROSS_NM']=pd.Series(np.empty(slength,dtype=np.chararray))
    processed_dat=crossing_nm(scaridat)
    processed_dat.to_csv(outfile, sep=',', index=False)



if __name__ == "__main__":
    main()
