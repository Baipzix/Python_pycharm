import arcpy
from datetime import datetime

inFeatures = r"\\Lacie-5big-pro\gis2\1_Data\5_Vector\1_Reference\LSD.shp"
outFeature = r"\\Lacie-5big-pro\gis2\1_Data\5_Vector\1_Reference\LSD_SEC.shp"
dissolveField = "SEC"

print(datetime.now())
arcpy.Dissolve_management(inFeatures, outFeature, dissolveField, "", "SINGLE_PART", "DISSOLVE_LINES")
print(datetime.now())
print("--end--")
