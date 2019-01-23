'''
Created on Sep 30, 2017

@author: haitaol
'''

import arcpy
import math



def streight(segment):
    pnt_st=segment.firstPoint
    pnt_en=segment.lastPoint
    len1=segment.length
    len2=math.sqrt((pnt_st.X-pnt_en.X)**2+(pnt_st.Y-pnt_en.Y)**2)
    if len2==0:
        return 0
    else: 
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
        
    if pnt_st.X<>pnt_en.X:
        gradient=(pnt_st.Y-pnt_en.Y)/(pnt_st.X-pnt_en.X)
    else:
        gradient=9999
    intercept=pnt_st.Y-gradient*pnt_st.X
    
    line_pmts=[gradient,intercept]
    return line_pmts
    
   
    

shp=r"C:\CLRP\naming\Treatment102_SJ_pmt.shp"
desc= arcpy.Describe(shp)
shpDes=desc.ShapeFieldName




fields=['gradient','intercept','stgh','fstX','fstY','lstX','lstY']


print("----")
    
cursor= arcpy.UpdateCursor(shp,fields)
for row in cursor:
    feat=row.getValue(shpDes)  
    xy1=feat.firstPoint
    xy2=feat.lastPoint

    line_prmts=lineparemeter(feat)
    stg=streight(feat)
    
    print(row.getValue((desc.OIDFieldName)),":  ",feat.partCount, line_prmts," ",stg)
    
    
    
    
    row.setValue("gradient", line_prmts[0])
    row.setValue("intercept", line_prmts[1])
    row.setValue("stgh", stg)
    row.setValue("fstX",xy1.X)
    row.setValue("fstY",xy1.Y)
    row.setValue("lstX",xy2.X)
    row.setValue("lstY",xy2.Y)
    
    
    
    
    cursor.updateRow(row)
    
    
del cursor, row
    
    
    
print("Fished the Processing")  
    
    
    

     
    
    