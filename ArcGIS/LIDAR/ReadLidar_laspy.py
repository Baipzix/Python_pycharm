#Testing the laspy library


from laspy.file import File
import numpy as np
import matplotlib.pyplot as plt





lifepath=r"\\Lacie-5big-pro\gis2\1_Data\4_LiDAR\2013_11_26_Apache_WapitiSimonette11822\Las\083k05i14.las"
outpath=r"C:\tmp\cls2.las"
lasfile=File(lifepath,mode='r')

I=lasfile.Classification==2

outFile=File(outpath, mode='w',header=lasfile.header)
outFile.points=lasfile.points[I]
print(outFile.points[0:5] )


pointform=outFile.point_format
for spec in pointform:
    print(spec.name)

print(outFile.gps_time[0:5])

gpstime=outFile.gps_time
height=outFile.Z
print(gpstime[0:1000])
print(height[0:1000])
outFile.close()

