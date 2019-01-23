import arcpy
from arcpy import env

#env.workspace=r"\\Lacie-5big-pro\gis2\1_Data\BC\dgtl_road_atlas.gdb\dgtl_road_atlas.gdb"
ftc=r"\\Lacie-5big-pro\gis2\1_Data\BC\dgtl_road_atlas_1.gdb\GBA\TRANSPORT_LINE"

att=[]
field='TRANSPORT_LINE_TYPE_CODE'

tableCs=arcpy.da.SearchCursor(ftc,field)
for row in tableCs:
     v=row[0]
     if not(v in att):
         att.append(v)
del tableCs




#
# table=r"\\Lacie-5big-pro\gis2\1_Data\BC\dgtl_road_atlas_1.gdb\TRANSPORT_LINE_TYPE_CODE"
#
# tableCs=arcpy.da.SearchCursor(ftc,field)
#
# for row in tableCs:
#     att.append(row[0])
# del tableCs
# print(att)

