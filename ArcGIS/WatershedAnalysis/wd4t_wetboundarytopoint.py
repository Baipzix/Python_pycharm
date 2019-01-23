import arcpy
import os


def listfile(dir):
    shplist=[]
    for root, subs, files in os.walk(dir):
        print(root)

        for file in files:
            if file.endswith(".shp"):
                shp = os.path.join(root, file)
                shplist.append(shp)

    return shplist

def areatopoint(shp):
    pointlist = []
    point = arcpy.Point()
    # find the mid one

    for row in arcpy.da.SearchCursor(shp, ["SHAPE@"]):
        for part in row[0]:
            pl=len(part)

            for pt in part:
                point.X=pt.X
                point.Y=pt.Y

                print('x--- ', pt.X, 'Y---  ', pt.Y)
                mpt=arcpy.PointGeometry(point)
                pointlist.append(mpt)


    return pointlist


def Georefer(orignialFile, file):
    spatial_ref = arcpy.Describe(orignialFile).spatialReference
    arcpy.DefineProjection_management(file, spatial_ref)


def main():
    folder=r'J:\2_FRIAA\Gold Lake_Caribou\data\test'
    shplist=listfile(folder)

    for shp in shplist:
        p1=areatopoint(shp)







    # np_point=np.asanyarray(points)
    # print(np_point)
    # print(np_point[:,2])
    # print(np_point[:,3])
if __name__ == "__main__":
    main()