import arcpy
import numpy as np
import pandas as pd


def FirstLastPoint(shp):
    clm = ['id', 'length', 'fx','fy','lx','ly']
    pointlist = pd.DataFrame(columns=clm)

    for row in arcpy.da.SearchCursor(shp, ["FID","SHAPE@", "Length"]):
        dt = np.array([np.arange(6)] * 1)
        df = pd.DataFrame(dt, columns=clm)

        startpoint = row[1].firstPoint
        endpoint = row[1].lastPoint

        df['id'] = row[0]
        df['length'] = row[2]
        df['fx'] = startpoint.X
        df['fy'] = startpoint.Y
        df['lx'] = endpoint.X
        df['ly'] = endpoint.Y

        pointlist = pointlist.append(df)
    return pointlist


def extractRaster(raster, point):
    #point or point list
    rastervalue=arcpy.GetCellValue_management(raster,point )
    return rastervalue

def sinuosity(points):
    stm_len=np.sqrt( np.power((points['fx']-points['lx']),2)+np.power((points['fy']-points['ly']),2))
    ss=points['length']/stm_len
    return ss




def main():
    stream = r'C:\tmp\WT4D\stream.shp'
    points = FirstLastPoint(stream)
    points['sinuosity']=sinuosity(points)


    # np_point=np.asanyarray(points)
    # print(np_point)
    # print(np_point[:,2])
    # print(np_point[:,3])
if __name__ == "__main__":
    main()