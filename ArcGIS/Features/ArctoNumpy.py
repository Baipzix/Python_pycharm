import arcpy
import numpy

input=r"V:\Shared\Ecology\Restoration\CLRP_Planning2017\Naming Convention\Seismic_Naming_Convention.shp"


shp=arcpy.da.FeatureClassToNumPyArray(input,('cmpt','direction','seismicID','sgmtID','fstX','fstY','OBJECTID'))

arr=shp[shp['seismicID']=="AA"]
#shp['cmpt']=="DV"][shp['direction']=="E"]
print(len(shp))
print(arr)
#print(arr.min())

# for row in shp:
#     print(row)