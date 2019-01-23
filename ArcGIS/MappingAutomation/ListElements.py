import arcpy, os, sys

import numpy
# read the mxd file
mxd_map=r"J:\2_TOLKO\2018 map\tolko.mxd"
path = os.path.dirname(sys.argv[0])
mxd=arcpy.mapping.MapDocument(mxd_map)
df=arcpy.mapping.ListDataFrames(mxd)

print(path)



lyrs=arcpy.mapping.ListLayers(mxd)
print(len(lyrs))
for lyr in lyrs:
    print(lyr)
print('---')
elments=arcpy.mapping.ListLayoutElements(mxd)
for elm in elments:
    print('name: ',elm.name)
    print(elm.text)
    print(elm)
    print('----')