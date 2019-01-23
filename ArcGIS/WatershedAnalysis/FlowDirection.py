import arcpy


def flowDir(dem):
    arcpy.sa.FlowDirection(in_surface_raster=dem, force_flow='NORMAL',
                           out_drop_raster=r'\\Lacie-5big-pro\gis2\2_SCARI\Berland_restoration_model\cubic30.gdb\fd_DEM_filter')
    print('Done')


def main():
    arcpy.CheckOutExtension("Spatial")
    dem = r'\\Lacie-5big-pro\gis2\2_SCARI\Berland_restoration_model\cubic30.gdb\DEM_Fill_filter'
    flowDir(dem )
    arcpy.CheckInExtension("Spatial")


if __name__ == "__main__":
    main()
