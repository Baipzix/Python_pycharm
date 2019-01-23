import arcpy
import glob
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
rasters=glob.glob(r"E:\CLRP\Compartments\data_analysis\ClippedRaster\msk*.tif")
shp=r"C:\tmp\slope\Seismic_FLMF_bf.shp"

outfd=r"C:\CLRP\ClippedRaster"

for raster in rasters:

    Extract_tif=raster.replace("msk","clp")
    print(Extract_tif)
    try:
        if not arcpy.Exists(Extract_tif):
            arcpy.gp.ExtractByMask_sa(raster, shp, Extract_tif)


    except Exception:
        print("Cannot convert " + raster + " to vector")
        e = sys.exc_info()[1]
        print(e.args[0])
    print(datetime.now())
# print(datetime.now())
# for cursors in arcpy.da.SearchCursor("twn",["PID"]):
#     print(cursors[0])
#     field=arcpy.AddFieldDelimiters(shp,"PID")
#     whereclause="{field}='{val}'".format(field=field,val=cursors[0])
#
#     #whereclause="\"PID\"="+str(cursors[0])
#
#
#     Extract_tif=outfd+r"\msk_"+str(cursors[0])+".tif"
#     print(whereclause)
#     print(Extract_tif)
#     arcpy.SelectLayerByAttribute_management("twn","CLEAR_SELECTION")
#     arcpy.SelectLayerByAttribute_management("twn","NEW_SELECTION", whereclause)
#     arcpy.gp.ExtractByMask_sa(raster, "twn", Extract_tif)
#     print(datetime.now())

# Values=list()
# with arcpy.da.SearchCursor(shp,["PID"]) as Scur:
#     for row in Scur:
#         Values.append(row[0])
# print(Values)
#
# for value in Values:
#     #whereclause="'"%s" = %s'" % ("PID",value)
#     whereclause = "\"PID\"=" + str(value)
#     print(whereclause)
#     arcpy.MakeFeatureLayer_management(shp, "twn",whereclause)
#
#     Extract_tif = outfd + r"\msk_" + str(value) + ".tif"
#     print(Extract_tif)
#     #try:
#         #out_raster=arcpy.sa.ExtractByMask(raster,"twn")
#     # out_raster.save(Extract_tif)
#
#     # except Exception:
#     #     e=sys.exc_info()[1]
#     #     print(e.args[0])
#
#
#     arcpy.Delete_management("twn")
#     print(datetime.now())


arcpy.CheckInExtension("spatial")