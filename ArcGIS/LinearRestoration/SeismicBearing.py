import arcpy
import math

def linebearing_degree(p1, p2):
    if p1.X > p2.X:
        x0 = p2.X
        y0 = p2.Y
        x1 = p1.X
        y1 = p1.Y
    else:
        x0 = p1.X
        y0 = p1.Y
        x1 = p2.X
        y1 = p2.Y
    try:
        tandegree = (y1 - y0) / (x1 - x0)
        direction= round(math.degrees(math.atan(tandegree)),2)
    except ZeroDivisionError:
        direction=90
        pass
    return direction

def linebearing_name(p1, p2):
    if p1.X > p2.X:
        x0 = p2.X
        y0 = p2.Y
        x1 = p1.X
        y1 = p1.Y
    else:
        x0 = p1.X
        y0 = p1.Y
        x1 = p2.X
        y1 = p2.Y
    try:
        tandegree = (y1 - y0) / (x1 - x0)
        if -0.2 <= tandegree <= 0.2:
            direction = 'EE'
        elif 0.2 < tandegree <= 10:
            direction = 'NE'
        elif tandegree > 10:
            direction = 'SS'
        elif -10 <= tandegree < -0.2:
            direction = 'SE'
        elif tandegree < -10:
            direction = 'SS'

    except ZeroDivisionError:
        direction=''
        pass
    return direction


def fDirection(shp):

    # for row in arcpy.da.UpdateCursor(shp, ["SHAPE@",  "FID"]):
    #     idpt=[]
    #     fpxy=row[0].firstPoint
    #     lpxy=row[0].lastPoint
    #
    #     if fpxy.X>lpxy.X:
    #         x0=lpxy.X
    #         y0=lpxy.Y
    #         x1=fpxy.X
    #         y1=fpxy.Y
    #     else:
    #         x0=fpxy.X
    #         y0=fpxy.Y
    #         x1=lpxy.X
    #         y1=lpxy.Y
    #
    #     try:
    #         bearing=(y1-y0)/(x1-x0)
    #     except ZeroDivisionError:
    #         pass
    #
    #
    #     if  -0.5<= bearing<=0.5:
    #         direction='EE'
    #     elif 0.5< bearing<=10:
    #         direction='NE'
    #     elif bearing> 10:
    #         direction='SS'
    #     elif -10 <=bearing<-0.5:
    #         direction='SE'
    #     elif bearing<-10:
    #         direction='SS'
    #
    #     idpt=[row[1], direction]
    #
    #     pointlist.append(idpt)
    # del row

    fields=['SHAPE@','OBJECTID', 'Bearing', 'Degree']
    with arcpy.da.UpdateCursor (shp, fields) as cursor:
        for row in cursor:
            fpxy = row[0].firstPoint
            lpxy = row[0].lastPoint
            row[2]=linebearing_name(fpxy,lpxy)
            row[3]=linebearing_degree(fpxy, lpxy)
            cursor.updateRow(row)
    del row
    del cursor

def main():
    line=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\TreatmentPrescriptions2.shp"
    fDirection(line)


if __name__ == "__main__":
    main()
