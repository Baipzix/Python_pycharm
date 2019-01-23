import arcpy
import numpy


def unique_value(table, field):
    with arcpy.da.SearchCursor(table,[field]) as cursor:
        return sorted({row[0] for row in cursor})

def unique_value_npy(table, field):
    data=arcpy.da.TableToNumPyArray(table,[field])
    return numpy.unique(data[field])


inFeature=r"C:\tmp\AVI_clipped.shp"



listFields=arcpy.ListFields(inFeature)

for field in listFields:
    print(field.name)
    print(unique_value(inFeature,field.name))
    print(unique_value_npy(inFeature,field.name))


year=unique_value_npy(inFeature,"ORIGIN")
