import arcpy


def CentroPoint(shp):
    pointlist = []
    point=arcpy.Point()
    for row in arcpy.da.SearchCursor(shp, ["SHAPE@"]):
        pxy=row[0].centroid
        point.X=pxy[0]
        point.Y=pxy[1]
        pointG=arcpy.PointGeometry(point)
        pointlist.append(pointG)
    return pointlist

#convert the intersect line of road and stream to a crossing
def MidPointofLine(shp):
    midpointlist = []
    point = arcpy.Point()
    # find the mid one

    for row in arcpy.da.SearchCursor(shp, ["SHAPE@"]):
        for part in row[0]:
            pl=len(part)
            point.X=part[pl/2].X
            point.Y=part[pl/2].Y
            mpt=arcpy.PointGeometry(point)
            midpointlist.append(mpt)
    return midpointlist

def FirstPoint(shp):
    pointlist = []
    point=arcpy.Point()
    for row in arcpy.da.SearchCursor(shp, ["SHAPE@"]):
        pxy=row[0].firstPoint
        point.X=pxy.X
        point.Y=pxy.Y
        pointG=arcpy.PointGeometry(point)
        pointlist.append(pointG)
    return pointlist


def ExportShp(plist, out_shp, org_shp):
    arcpy.CopyFeatures_management(plist, out_shp)
    spatial_ref = arcpy.Describe(org_shp).spatialReference
    arcpy.DefineProjection_management(out_shp, spatial_ref)


line=r'\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\crossings\landusecrossing\road_enc_dsv.shp'
output_shp=r'\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\crossings\landusecrossing\road_enc_dsv_pt.shp'


midpt=MidPointofLine(line)
#midpt=FirstPoint(line)
ExportShp(midpt,output_shp,line)

#fstpt=CentroPoint(line)
#for pt in fstpt:
#    print(pt)




