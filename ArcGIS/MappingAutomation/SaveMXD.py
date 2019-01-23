import arcpy, os, sys
from datetime import datetime
import numpy
import glob
# read the mxd file
# mxd_map=r"C:\CNRL\Berland3.mxd"
#
# mxd=arcpy.mapping.MapDocument(mxd_map)
# mxd2=arcpy.mapping.MapDocument(r"C:\CNRL\Berland4.mxd")
#
#
# print (datetime.now())
# #arcpy.mapping.ExportToPNG(mxd,r"C:\CNRL\Berland_TBK.png",df_export_height=1728, df_export_width=2592, resolution=300)
# arcpy.mapping.ExportToPNG(mxd2,r"C:\CNRL\Berland_sm.png", resolution=96)
# #arcpy.mapping.ExportToJPEG(mxd,r"C:\CNRL\Berland_TBK.jpg", resolution=96)
# print (datetime.now())
# #arcpy.mapping.ExportToJPEG(mxd,r"C:\CNRL\Berland_TBK.jpg", df_export_width=2592,df_export_height=1728, resolution=300)
# arcpy.mapping.ExportToJPEG(mxd2,r"C:\CNRL\Berland_crossingtop.jpg", df_export_width=2592,df_export_height=1728, resolution=300)
print (datetime.now())



#----------------


mxd_list=glob.glob(r'J:\2_Bonavista\Nov30\*.mxd')


for mxdname in mxd_list:
    print(mxdname)
    outpdf=mxdname.replace('mxd','pdf')
    outjpg=mxdname.replace('mxd','jpg')
    mxd=arcpy.mapping.MapDocument(mxdname)
    # arcpy.mapping.ExportToPDF(mxd,outpdf,data_frame='PAGE_LAYOUT',df_export_height=640,df_export_width=480,
    #                           resolution=300,image_quality='BEST',colorspace='RGB',compress_vectors=True,
    #                           image_compression='DEFLATE',picture_symbol='VECTORIZE_BITMAP',convert_markers=False,
    #                           embed_fonts=False,layers_attributes='LAYERS_ONLY',georef_info=True)

    arcpy.mapping.ExportToPDF(mxd, out_pdf=outpdf,picture_symbol='VECTORIZE_BITMAP',embed_fonts=False,georef_info=True)
    #arcpy.mapping.ExportToJPEG(mxd,out_jpeg=outjpg,resolution=200)
    del mxd


    print(datetime.now())

print('---end---')
