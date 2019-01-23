import arcpy
import glob
import os
import sys

workfolder=r""
rasterlist=glob.glob(r'\\Lacie-5big-pro\\gis2\\1_Data\\4_LiDAR\\201804_M15_Berland\\3_LiDAR\\2_LiDAR_Delivery Areas\\**\\**\\*.asc')


# resample
cell_size=2
resample_list=[]
errorlist=[]
for raster in rasterlist:
    rastername=raster.replace('bare_earth_DEM_ascii','resample_2m')
    resample_raster=rastername.replace('.asc','.tif')
    resample_list.append(resample_raster)
    print(raster)
    # print(resample_raster)
    try:
        arcpy.Resample_management(raster,resample_raster,  cell_size, resampling_type="NEAREST")
    except Exception:
        e=sys.exc_info()[1]
        print(e.args[0])
        errorlist.append(raster)


print(len(resample_list))

# for raster in rasterlist:
#     fdir, rname = os.path.split(raster)
#     print(fdir)
#     print(rname)

#
# resample_list=rasterlist
# print('merge raster')
# arcpy.MosaicToNewRaster_management(resample_list,output_location=r"J:\1_Data\2_DEM\BC_DEM_L",
#                                    raster_dataset_name_with_extension="BCDEM_L_20m.tif",number_of_bands=1,
#                                    mosaic_method="LAST")
#
#
# print('hill shade')
# dem=r"J:\1_Data\2_DEM\BC_DEM_L\BCDEM_L_20m.tif"
#
#
# if arcpy.CheckExtension("3D")=="Available":
#     arcpy.CheckOutExtension("3D")
# if arcpy.CheckExtension("Spatial")=="Available":
#     arcpy.CheckOutExtension("Spatial")
# for raster in rasterlist:
#     dir, fname=os.path.split(raster)
#     dir=os.path.dirname(raster)
#     print(fname)
#     hsh=r"J:\1_Data\2_DEM\BC_DEM_L\\"+fname.replace('utm','hsh')
#     print(hsh)
#     arcpy.HillShade_3d(raster, hsh)
#
#
#
#
#     #arcpy.HillShade_3d(raster, hsh)
#
#



print('---------done-------')