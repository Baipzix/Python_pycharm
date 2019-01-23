import arcpy

def FirstLastPoint(shp):
    pointlist = []
    # point=arcpy.Point()
    for row in arcpy.da.SearchCursor(shp, ["FID","SHAPE@", "Length"]):
        segement=[]
        print(row[0])
        segement.append(row[0])
        segement.append(row[2])
        startpoint=row[1].firstPoint
        endpoint=row[1].lastPoint

        segement.append(startpoint.X)
        segement.append(startpoint.Y)
        segement.append(endpoint.X)
        segement.append(endpoint.Y)

        pointlist.append(segement)
        # pxy=row[0]
        # point.X=pxy[0]
        # point.Y=pxy[1]
        # pointG=arcpy.PointGeometry(point)
        # pointlist.append(pointG)
    return pointlist



line=r"C:\tmp\WT4D\stream.shp"

points=FirstLastPoint(line)
print(points)
#rows=[row for row in arcpy.da.SearchCursor(line,["SHAPE@XY"])]

# for part in rows[1]:
#     print(part)
#     for pnt in part:
#         if pnt:
#             print("{ },{ }".format(pnt.X,pnt.Y))
# #for row in arcpy.da.SearchCursor(line,["FID"]):
# for row in arcpy.da.SearchCursor(line, ["FID", "SHAPE@X", "SHAPE@Y", "SHAPE@JSON"]):
#     # Print x,y coordinates of each point feature
#     #
#
#     xf.yf=row.firstPoint
#     xl,yl=row.lastPoint
#     print(xf, xy)
#     print(xl,yl)
#     print(row[0])
#     print("--")