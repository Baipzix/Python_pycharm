import arcpy

line=r"C:\tmp\WT4D\stream.shp"
rownum=0
pointlist=[]
#### loop lines and search the
 for row in arcpy.da.SearchCursor(line,["SHAPE@"]):
    #print ("Feature".format((row[0])))
    rownum+=1
    partnum = 0

    print("-------------")
    for part in row[0]:
        #partnum+=1

        for pnt in part:
            if pnt:
                xy=[pnt.X, pnt.Y]
                pointlist.append(xy)
    print(partnum)

print(rownum)

# inFeatures=r'C:\tmp\WT4D\stream.shp'
outFeature=r'C:\tmp\WT4D\streams_pt1.shp'
# arcpy.FeatureToPoint_management(inFeatures, outFeature)
#


# pt=arcpy.Point()
# pt_fts=[]
# for p in pointlist:
#     pt.X=p[0]
#     pt.Y=p[1]
#     pt_fts.append(arcpy.PointGeometry(pt))
# arcpy.CopyFeatures_management(pt_fts, outFeature )

spatial_ref=arcpy.Describe(line).spatialReference
print(spatial_ref.name)
ProOutput=r"C:\tmp\WT4D\streams_prj.shp"
arcpy.DefineProjection_management(outFeature,spatial_ref)


