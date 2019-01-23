
import arcpy
import glob

rasterlist=glob.glob('J:/1_Data/2_DEM/**/**/cdem_dem_*.tif')

# Local variables:

cdem_dem_094P_ProjectRaster = "C:\\Users\\haitaol\\Documents\\ArcGIS\\Default.gdb\\cdem_dem_094P_ProjectRaster"

for raster in rasterlist:
    reproject_raster = raster.replace('.tif', '_utm.tif')
    arcpy.ProjectRaster_management(raster, reproject_raster,
                                   "PROJCS['NAD_1983_UTM_Zone_10N'," \
                                   "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',"
                                   "SPHEROID['GRS_1980',6378137.0,298.257222101]]," \
                                   "PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]," \
                                   "PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0]," \
                                   "PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0]," \
                                   "PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0]," \
                                   "UNIT['Meter',1.0]]", "NEAREST", "20 20",
                                   "'NAD_1983_CSRS_To_WGS_1984_2 + WGS_1984_(ITRF00)_To_NAD_1983'","",
                                   "GEOGCS['GCS_North_American_1983_CSRS',"
                                   "DATUM['D_North_American_1983_CSRS',SPHEROID['GRS_1980',6378137.0,298.257222101]]," \
                                   "PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")


    print(reproject_raster)

print('---done--')