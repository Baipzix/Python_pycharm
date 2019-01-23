import arcpy
from datetime import datetime
import sys

arcpy.CheckOutExtension("spatial")
def listFieldName(shp):
    fields=arcpy.ListFields(shp)
    fieldList=[]
    for field in fields:
        fieldList.append(field.name)
    return fieldList


#raster=r"C:\CLRP\LittleSmoky_ht_Recls_ClipCopy.tif"
shp=r"C:\tmp\slope\Seismic_twn.shp"

outfd=r"C:\CLRP\ClippedRaster"

fieldName=listFieldName(shp)
print(fieldName)
arcpy.MakeFeatureLayer_management(shp, "twn")

print(datetime.now())
for cursors in arcpy.da.SearchCursor("twn",["PID"]):
    print(cursors[0])
    field=arcpy.AddFieldDelimiters(shp,"PID")
    whereclause="{field}='{val}'".format(field=field,val=cursors[0])

    #whereclause="\"PID\"="+str(cursors[0])


    Extract_tif=outfd+r"\clip_"+str(cursors[0])+".tif"
    print(whereclause)
    print(Extract_tif)
    arcpy.SelectLayerByAttribute_management("twn","CLEAR_SELECTION")
    arcpy.SelectLayerByAttribute_management("twn","NEW_SELECTION", whereclause)
    arcpy.gp.ExtractByMask_sa(raster, "twn", Extract_tif)
    print(datetime.now())



arcpy.CheckInExtension("spatial")