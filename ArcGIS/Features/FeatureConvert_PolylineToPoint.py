import numpy as np
import arcpy
import sys
from os import listdir
import os
import glob
from datetime import datetime

def splitter(g, gn):
    k,m=divmod(len(g),gn)
    return (g[i*k+min(i,m):(i+1)*k + min(i+1,m)] for i in xrange(gn))

def pointToGeo(pointlist):
    pt = arcpy.Point()
    pt_fts = []
    for p in pointlist:
        pt.X = p[0]
        pt.Y = p[1]
        pt_fts.append(arcpy.PointGeometry(pt))
    return pt_fts

def mergeShp(path, prefix, originalFile):
    base = os.path.basename(originalFile)
    flist = glob.glob(path+prefix+"*.shp")
    Mgshpfile = path + "points_of_" + base
    try:
        arcpy.Merge_management(flist, Mgshpfile)
    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
        e = sys.exc_info()[1]
        print(e.args[0])
        print("cannot merge shapefiles")

    # delete tmp shp
    try:
        if len(flist)<1:
            arcpy.Delete_management(flist)
        else:
            for shpf in flist:
                arcpy.Delete_management(shpf)
    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
        e = sys.exc_info()[1]
        print(e.args[0])
        print("cannot delete shapefiles, it may be using or not exist.")
    return Mgshpfile

def Georefer(orignialFile, file):
    spatial_ref = arcpy.Describe(orignialFile).spatialReference
    arcpy.DefineProjection_management(file, spatial_ref)




def main():
    inFeature = r'J:\2_FRIAA\Gold Lake_Caribou\Stream_1m_10k.shp'
    outpath = r'\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\\'
    prefix = r"Tmp_"
    maxpointnum = 300000
    pointlist = []

    #Read Vertices points and save x y value into pointlist
    for row in arcpy.da.SearchCursor(inFeature, ["SHAPE@"]):
        for part in row[0]:
            for pnt in part:
                if pnt:
                    xy = [pnt.X, pnt.Y]
                    pointlist.append(xy)
    pointsnum = len(pointlist)



    # split the points to smaller group and convert them to shp
    if pointsnum < maxpointnum:
        Geopoint = pointToGeo(pointlist)
        base = os.path.basename(inFeature)
        outShp = outpath + "points_of_" + base
        arcpy.CopyFeatures_management(Geopoint, outShp)
    else:
        group_num = int(pointsnum / maxpointnum)
        glist = splitter(range(pointsnum), group_num)
        points_np = np.asanyarray(pointlist)
        for subindex in glist:
            subpoints = points_np[np.array(subindex)]
            Geopoint = pointToGeo(subpoints)
            try:
                outFeature = outpath + prefix + str(subindex[0]) + ".shp"
                arcpy.CopyFeatures_management(Geopoint, outFeature)
            except arcpy.ExecuteError:
                print(arcpy.GetMessages())
                e = sys.exc_info()[1]
                print(e.args[0])
                print("cannot save as shapefile")

        # merge all shapefile
        outShp = mergeShp(outpath, prefix, inFeature)

    # Georeference
    Georefer(inFeature, outShp)



if __name__ == "__main__":
    start_time=datetime.now()
    main()
    print(datetime.now()-start_time)


