'''
Created on Oct 2, 2017

@author: haitaol
'''

import arcpy


shp=r"C:\tmp\seismic_misline.shp"


fields = ["cmpt","direction","seismicID","sgmtID","Name"]




cursor= arcpy.UpdateCursor(shp,fields)
for row in cursor:
    cmpt=row.getValue(fields[0])
    direction=row.getValue(fields[1])
    seismicID=row.getValue(fields[2])
    sgmtID=row.getValue(fields[3])
    
    

    newID=cmpt+"_"+direction+"_"+seismicID+"_"+sgmtID
    print(newID)
    row.setValue("Name",newID)
    cursor.updateRow(row)
    


del cursor, row

print ("Finished")