import arcpy
import os
import fnmatch
from datetime import datetime

def folder_in_dir(top_dir, folder_name):
    folderList=[]
    for fn in os.listdir(top_dir):
        folddir=os.path.join(top_dir,fn)
        #print(folddir)

        if os.path.isdir(folddir):
            if fn.upper()==folder_name.upper():
                folderList.append(folddir)
            else:
                folderList+=folder_in_dir(folddir, folder_name)
    return folderList


def listFiles(dir, ext_name):
    flist=[]
    listF=os.listdir(dir)
    for f in listF:
        if fnmatch.fnmatch(f, ext_name):
            flist.append(os.path.join(dir,f))
    return flist



print('------------------')
print(datetime.now())
top_dir=r"J:\1_Data\4_LiDAR\201804_M15_Berland\3_LiDAR\2_LiDAR_Delivery Areas"
folder_name="DEM_mosaic"

ext="*.tif"
max_raster_nm=100
output_raster=r"J:\1_Data\4_LiDAR\201804_M15_Berland\3_LiDAR\2_LiDAR_Delivery Areas\Mosaic"

folderlist=folder_in_dir(top_dir,folder_name)
print(folderlist)

# loop folder where has raster files
for folder in folderlist:
    rasterlist=listFiles(folder,ext)
    rn=len(rasterlist)
    print(folder)
    str_folder=str(folder)
    starti=str_folder.rfind(' ')
    endi=str_folder.rfind('\\')
    raster_name='Aear_'+str_folder[starti+1:endi]
    print("total raster:"+str(rn))
    if rn<=max_raster_nm:
        print(rn)
        #mosaic
        t1=datetime.now()
        arcpy.MosaicToNewRaster_management(rasterlist,output_location=output_raster,raster_dataset_name_with_extension=raster_name+'.tif',
                                         pixel_type="32_BIT_FLOAT", cellsize=2,number_of_bands=1)
        t2=datetime.now()
        print(t2-t1)
    else:
        #set group size

        group_size=rn/(rn/max_raster_nm+1)+1
        print("sub group size: "+str(group_size))
        #subside group
        i = 0
        while i < rn:
            sub_group = rasterlist[i:i + group_size]
            #print(sub_group)
            i = i + group_size
            sub_name=raster_name+"_"+str(i)
            print('raster name: '+sub_name+'.tif')
            t1=datetime.now()
            arcpy.MosaicToNewRaster_management(sub_group, output_location=output_raster,
                                               raster_dataset_name_with_extension=sub_name+'.tif',
                                               pixel_type="32_BIT_FLOAT", cellsize=2, number_of_bands=1)
            t2=datetime.now()
            print(t2-t1)



print(datetime.now())
print('---end----')

