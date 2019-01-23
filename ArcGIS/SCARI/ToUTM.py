import utm
import pandas as pd
import numpy as np
# convert to utm

def conv_utm(lat, long, dat):
    latlen=len(lat)
    longlen=len(long)

    east = np.zeros((latlen))
    north= np.zeros((latlen))
    zone= np.zeros((latlen))

    ewn=np.empty([])

    if latlen==longlen:
        print(latlen)
        for i in xrange(latlen):
            utm_info = utm.from_latlon(lat[i], long[i])
            #print(utm_info)
            east[i]=utm_info[0]
            north[i] = utm_info[1]
            zone[i] = utm_info[2]


        dat['EAST']=east
        dat['NORTH']=north
        dat['ZONE']=zone
        dat.to_csv(r"J:\2_Enbridge\2018\Crossings.csv\crossing_latlong_eastnorth.csv", sep=',', index=False)
    else:
        print(r'lat long doesn\'t match')





# read csv

# main

def main():

    csvfile=r"J:\2_Enbridge\2018\Crossings.csv"
    latlong = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)

    lat=latlong['LAT'].values
    long=latlong['LONG'].values

    conv_utm(lat,long, latlong)


if __name__ == "__main__":
    main()
