'''
Created on Sep 27, 2017

@author: haitaol
'''
import arcpy
import glob
import sys
from datetime import datetime

folder=r"W:\CLRP\Compartments\data_analysis\ClippedRaster"

#rasters=glob.glob(r"W:\CLRP\Compartments\data_analysis\msk*.tif")
rasters=[r"W:\CLRP\Compartments\data_analysis\ClippedRaster\msk_526060.tif",r"W:\CLRP\Compartments\data_analysis\ClippedRaster\msk_601059.tif",
         r"W:\CLRP\Compartments\data_analysis\ClippedRaster\msk_601060.tif",r"W:\CLRP\Compartments\data_analysis\ClippedRaster\msk_602058.tif"]
print (datetime.now())
for raster in rasters:
    try:
        print(raster)

        rname=raster.replace(".tif","")
        out_polygon_features=rname.replace("msk","msk_vector.gdb\\msk")
        print(out_polygon_features)

        if not arcpy.Exists(out_polygon_features):
            arcpy.RasterToPolygon_conversion(raster, out_polygon_features,"NO_SIMPLIFY","VALUE")

    except Exception:
        print("Cannot convert "+raster+" to vector")
        e=sys.exc_info()[1]
        print(e.args[0])
    print(datetime.now())

