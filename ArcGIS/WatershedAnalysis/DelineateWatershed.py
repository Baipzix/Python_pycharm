class LicenseError(Exception):
    pass


import arcpy
from arcpy import env
from arcpy.sa import *
import os
import glob


def delineatewatershed(inFlowD, point_shp):
    field = "grid_code"
    cursor = arcpy.SearchCursor(point_shp,fields="grid_code")
    arcpy.MakeFeatureLayer_management(point_shp, 'points')
    for row in cursor:
        p_nm = row.getValue(field)
        print(p_nm)
        whereClause = ''' "grid_code" = {} '''.format(p_nm)
        print(whereClause)
        arcpy.SelectLayerByAttribute_management("points", "NEW_SELECTION", whereClause)
        outWatershed = Watershed(inFlowD, 'points', field)
        outws = r"J:\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\crossingwatershed\swanhill_"\
                + str(p_nm) + ".tif"

        outWatershed.save(outws)

        print(outws)


def rastertopolygon(path, prefix):
    #search for all str
    flist = glob.glob(path+"\\"+prefix+"*.tif")
    for fraster in flist:
        print(fraster)
        outpolygon=fraster.replace(".tif",".shp")
        print(outpolygon)
        if not arcpy.Exists(outpolygon):
            arcpy.RasterToPolygon_conversion(fraster,outpolygon,"NO_SIMPLIFY", "VALUE")
        cleanpolygon(outpolygon)



def cleanpolygon(shp):
    #print(shp)
    filename=os.path.basename(shp)
    #print(filename)
    d1=filename.index('_')+1
    d2=filename.index('.')
    value=int(filename[d1:d2])
    #print(value)
    arcpy.MakeFeatureLayer_management(shp,filename)
    whereClause = ''' "GRIDCODE" <> {} '''.format(value)
    arcpy.SelectLayerByAttribute_management(filename,"NEW_SELECTION",whereClause)
    if int(arcpy.GetCount_management(filename).getOutput(0))>0:
        arcpy.DeleteFeatures_management(filename)


def main():
    try:
        if arcpy.CheckExtension("Spatial")=="Available":
            arcpy.CheckOutExtension("Spatial")
        else:
            raise LicenseError
        arcpy.env.extent=r'\\Lacie-5big-pro\gis2\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\SwanHill.gdb\smooth_stream'
        inFlowD = r'\\Lacie-5big-pro\gis2\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\SwanHill.gdb\FlowDir'
        pourpoint = r'\\Lacie-5big-pro\gis2\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\SwanHill.gdb\snappoint25'
        delineatewatershed(inFlowD, pourpoint)

    except LicenseError:
        print("license is unavailable")
    finally:
        arcpy.CheckInExtension("Spatial")

    shppath=r''
    rastertopolygon(r"J:\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\crossingwatershed", "swanhill_")


if __name__ == "__main__":
    main()
