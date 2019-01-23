'''
Created on Sep 26, 2017

@author: haitaol
'''


import arcpy
import math


def streight(segment):
    pnt_st=segment.firstPoint
    pnt_en=segment.lastPoint
    len1=segment.length
    len2=math.sqrt((pnt_st.X-pnt_en.X)**2+(pnt_st.Y-pnt_en.Y)**2)
    return len1/len2

def lineparemeter(segment):
    pnt_1=segment.firstPoint
    pnt_2=segment.lastPoint
    
    
    if (pnt_1.X<pnt_2.X):
        pnt_st=pnt_1
        pnt_en=pnt_2
    else:
        pnt_st=pnt_2
        pnt_en=pnt_1
        
    
    gradient=(pnt_st.Y-pnt_en.Y)/(pnt_st.X-pnt_en.X)
    intercept=pnt_st.Y-gradient*pnt_st.X
    
    line_pmts=[gradient,intercept]
    return line_pmts
    
   
    

shp=r"C:\Users\haitaol\Documents\ArcGIS\Default.gdb\D67V_Dissolve"
desc= arcpy.Describe(shp)
shpDes=desc.ShapeFieldName


for row in arcpy.SearchCursor(shp):
    #print(row.getValue("Shape_Length"))

    feat=row.getValue(shpDes)
    xy1=feat.firstPoint
    xy2=feat.lastPoint
    print(xy1)
    print(xy2)
    line_prmts=lineparemeter(feat)
    stg=streight(feat)
    row.update()
    row.setValue('gradient', line_prmts[0])
    row.setValue('intercept', line_prmts[1])
    row.setValue('straightness', line_prmts[1])
    

    
    print(row.getValue((desc.OIDFieldName)),":  ",feat.partCount, line_prmts," ",stg)




    
    
    