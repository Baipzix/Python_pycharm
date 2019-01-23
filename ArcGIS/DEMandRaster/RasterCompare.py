import arcpy


slope=[r"C:\tmp\slope\slope_gp.tif",r"C:\tmp\slope\slope_3d.tif",r"C:\tmp\slope\slope_sa.tif"]

compareFile=[r"C:\tmp\slope\gp_3d.txt",r"C:\tmp\slope\3d_sa.txt",r"C:\tmp\slope\gp_sa.txt"]
arcpy.RasterCompare_management(slope[0],slope[1],"RASTER_DATASET","","CONTINUE_COMPARE",compareFile[0],"","")
arcpy.RasterCompare_management(slope[1],slope[2],"RASTER_DATASET","","CONTINUE_COMPARE",compareFile[1],"","")
arcpy.RasterCompare_management(slope[0],slope[2],"RASTER_DATASET","","CONTINUE_COMPARE",compareFile[2],"","")