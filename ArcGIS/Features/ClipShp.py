import arcpy
import os

outpath=r'V:\Shared\Watercourse Crossings\CNRL_2018\subwatershed\MissingRoad'
#clip list
Fc_list=[r'V:\Shared\AltaLIS_DiDs\20180313121245\DAB_APPL.shp',
         r'V:\Shared\GIS\Alberta Human Footprint\2014\HFI2014_FTv2.gdb\o03_Roads_HFI2014',
         r'V:\Shared\GIS\Alberta Human Footprint\2014\HFI2014_FTv2.gdb\o20_SeismicLines_HFI2014',
         r'V:\Shared\GIS\Alberta Human Footprint\2014\HFI2014_FTv2.gdb\o19_Pipelines_HFI2014']

#NTS 50K
clip_shp=r'V:\Shared\GIS\AB_Reference\NTS_1_50k.shp'
clip_boundary=['83E09','83E10','83E15','83E16','83F13','83F14','83K03','83K04','83L01','83L02']

#make selection
ly=r'C:\tmp\nts_layer'
arcpy.MakeFeatureLayer_management(clip_shp,out_layer=ly)
arcpy.SelectLayerByAttribute_management(ly, selection_type="NEW_SELECTION",
                                        where_clause='"NTS50K" in '+ str(tuple(clip_boundary)) )



#clip
for fc in Fc_list:
    h,t=os.path.split(fc)
    h2,e=os.path.splitext(fc)

    if e!='.shp':
        outfc=os.path.join(outpath,t)+'.shp'
    else:
        outfc=os.path.join(outpath,t)
    arcpy.Clip_analysis(fc,ly,outfc)
    print(outfc)



print('-----end-----')

