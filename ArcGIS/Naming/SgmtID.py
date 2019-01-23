'''
Created on Sep 30, 2017

@author: haitaol
'''
import arcpy 



shp=r"C:\tmp\seismic_misline.shp"


fields = ["sgmtID"]

desired_length = 4



cursor= arcpy.UpdateCursor(shp,fields)
for row in cursor:
    sgID=row.getValue(fields[0])
    

    
    if len(sgID)<desired_length:
        zeros=desired_length-len(sgID)
        
        leading0=""
        add0=0
        
        while add0<zeros:
            leading0 += "0"
            add0 += 1
           
        newID=leading0+ sgID
        print(newID)
        row.setValue("sgmtID",newID)
        cursor.updateRow(row)
    


del cursor, row

print ("Finished")