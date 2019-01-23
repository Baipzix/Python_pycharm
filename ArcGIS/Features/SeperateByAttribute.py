import arcpy
import numpy
import os

def unique_fieldValue(fc, fieldName):
    #data=arcpy.da.TableToNumPyArray(fc,fieldName)
    with arcpy.da.SearchCursor(fc,fieldName) as cursor:
        return sorted({row[0] for row in cursor})




# input feature
fc=r'V:\Shared\Watercourse Crossings\CNRL_2018\subwatershed\MissingRoad\DAB_APPL.shp'
outpath=r'V:\Shared\Watercourse Crossings\CNRL_2018\subwatershed\MissingRoad\dids_layers'
#read field and list unique value

valuelist=unique_fieldValue(fc,'DISP_TYPE')
print(valuelist)
#make selection
ly = r'C:\tmp\nts_layer'
arcpy.MakeFeatureLayer_management(fc, out_layer=ly)

for fv in valuelist:
    print(fv)
    arcpy.SelectLayerByAttribute_management(ly, selection_type="NEW_SELECTION",
                                            where_clause='"DISP_TYPE" = \''+ fv+'\'')
    # copy selection
    outfc=os.path.join(outpath, fv+'.shp')
    arcpy.CopyFeatures_management(ly,outfc)

    print(outfc)

print('----end----')

