import arcpy

inFeature=r"V:\Shared\GIS\HUC8\HUC8_simple.shp"

fields=arcpy.ListFields(inFeature)

# for field in fields:
#     print("{0} is type of  {1} with a length of {2}"
#           .format(field.name, field.type, field.length))


fieldnames=[f.name for f in arcpy.ListFields(inFeature)]
for fieldname in fieldnames:
    print(fieldname)


#drop field name

dropfield=[u'HUC_6', u'HUC_4', u'HUC_2', u'WSC_CODE',  u'SHAPE_STLe']
arcpy.DeleteField_management(inFeature,dropfield)

fieldnames=[f.name for f in arcpy.ListFields(inFeature)]

print(fieldnames)
