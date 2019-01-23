'''
Created on Oct 3, 2017

@author: haitaol
'''


import arcpy 
import numpy as np

def direction(d_arr):

    fE=np.count_nonzero(d_arr=="E")
    #print(fE)
    fN=np.count_nonzero(d_arr=="N")
    #print(fN)
    if fE>=fN:
        return "E"
    else:
        return "N"


def sgmtOrder(sg_arr):    
    return sg_arr.argsort().argsort()


def order_str(oldID):
    desired_length=4
    arr_len=len(oldID)
    if arr_len<desired_length:
        zeros=desired_length-arr_len
    
    leading0=""
    add0=0
    
    while add0<zeros:
        leading0 += "0"
        add0 += 1
    newID=leading0 + oldID
    return newID
    

def sgID(shp, fields, fctID_arr, sgmtID_arr): 
    #fields=['FID','sgmtID'] 
    cursor=arcpy.UpdateCursor(shp, fields)
    for row in cursor:
        fid=row.getValue(fields[0])
        #print(fid)
        i=fctID_arr.index(fid)   
        row.setValue("sgmtID",sgmtID_arr[i])
        cursor.updateRow(row)      
    del cursor, row
    
    
    
def newName(shp, fields):
    #fields = ["cmpt","direction","seismicID","sgmtID","Name"]
    cursor= arcpy.UpdateCursor(shp,fields)
    for row in cursor:
        cmpt=row.getValue(fields[0])
        direction=row.getValue(fields[1])
        seismicID=row.getValue(fields[2])
        sgmtID=row.getValue(fields[3])
        newID=cmpt+"_"+direction+"_"+seismicID+"_"+sgmtID
        #print(newID)
        row.setValue(fields[4],newID)
        cursor.updateRow(row)
    del cursor, row




shp=r"C:\CLRP\naming\Treatment102_SJ_newName.shp"

shpArr=arcpy.da.FeatureClassToNumPyArray(shp,('FID','seismicID','direction','fstX','lstX','fstY','lstY'))
ScmcuniqID=np.unique(shpArr['seismicID'])

#ScmcuniqID=["AB"]
sgmtID_arr=[]
fid_arr=[]
for scid in ScmcuniqID:
    print(scid)
    arr=shpArr[shpArr['seismicID']==scid]
    #print(arr['direction'])

    d=direction(arr['direction'])
    
    if d=="E":
        xMin=np.minimum(arr['fstX'],arr['lstX'])
        order_arr=sgmtOrder(xMin)+1
        
    elif d=="N":
        yMin=np.minimum(arr['fstY'],arr['lstX'])
        order_arr=sgmtOrder(yMin)+1
    print(order_arr)
    
    
    newID_arr=[]
    for oldID in order_arr:
        idStr=str(oldID)
        newID=order_str(idStr)
        newID_arr.append(newID) 
    #print(newID_arr)
    sgmtID_arr.extend(newID_arr)
    fid_arr.extend(arr['FID'])
    

print(len(sgmtID_arr))
#print(sgmtID_arr)
print(len(fid_arr))
#print(fid_arr)
fields=['FID','sgmtID']
sgID(shp, fields, fid_arr, sgmtID_arr)

fields = ["cmpt","direction","seismicID","sgmtID","FullID"]
newName(shp, fields)



print(" ----naming convention is finished ")
