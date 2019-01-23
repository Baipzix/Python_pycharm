import arcpy




#list the field


#add the field


#remove the field



infcs=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\CHRP_Deliverable.gdb\toCompartmentwithHw"
cleanfcs=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\CHRP_Deliverable.gdb\toCompartmentwithHw3"
# arcpy.CopyFeatures_management(infcs, cleanfcs)
#
#
# fields=arcpy.ListFields(cleanfcs)
#
# fieldname=[f.name for f in fields]
#
# print(fieldname)

droplist=[u'UNIQ_NUM', u'DISP_TYPE', u'VER_DATE', u'DOC', u'DISC_FLAG', u'EDIT_DATE', u'PRO_DATE', u'TYPENAME', u'APPDATE', u'LOADATE', u'EFFDATE', u'AMNDATE', u'CANDATE', u'RENDATE', u'EXPDATE', u'REIDATE', u'AMLDATE', u'PLAN', u'STATCD', u'NEARWATER', u'PURPCD', u'PURPTXT', u'DIMENSION', u'AREA_Hect', u'AREA_Acres', u'CLIENTCD', u'COMPANY', u'FNAME', u'LNAME', u'CCOUNT', u'RESTCD', u'RESTEX1', u'RESTEX2', u'RESTEX3', u'RESTEX4', u'ADDRSTATUS', u'ADDRCD', u'ADDRESS1', u'ADDRESS2', u'ADDRESS3', u'ADDRESS4', u'ADDRESS5', u'CITY', u'PROVINCE', u'COUNTRY', u'POSTALCODE', u'ATTENTION', u'GENCMT']

arcpy.DeleteField_management(cleanfcs,droplist)
fields=arcpy.ListFields(cleanfcs)

fieldname=[f.name for f in fields]

print(fieldname)