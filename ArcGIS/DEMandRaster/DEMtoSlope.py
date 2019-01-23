import arcpy
#from arcpy.sa import *
from datetime import datetime


dem=r"C:\tmp\DP_dem.tif"

slope=[r"C:\tmp\slope\CLRP_DP_slope.tif"]
#,r"C:\tmp\slope\slope_3d.tif",r"C:\tmp\slope\slope_sa.tif"]
output_measurement = "PERCENT_RISE"
print(datetime.now())


# Process: Slope
arcpy.CheckOutExtension("Spatial")
# try:
#     arcpy.gp.Slope_sa(dem, slope[0], output_measurement, "1")
# except:
#     print("no gp")
# print(datetime.now())
# # Process: Slope (2)
print("process 3d slop")

arcpy.Slope_3d(dem, slope[0], output_measurement, "1")


print(datetime.now())
# print("process sa")
#
# try:
#     outSlope = Slope(dem, output_measurement, "1")
#     outSlope.save(slope[2])
# except:
#     print("no sa")
# print(datetime.now())

arcpy.CheckInExtension("Spatial")