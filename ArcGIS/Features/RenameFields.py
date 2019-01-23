
import arcpy

def listfieldProp(shp):
    fields=arcpy.ListFields(shp)
    for field in fields:
        print("Field Name:  ", field.name, " || Field type: ", field.type, " || Field length: ", field.length)

def addfields(shp, flist, ftype, flen):
    listlength=len(flist)
    for i in range(listlength):
        print(flist[i], ftype[i], flen[i])
        if ftype[i]=='FLOAT' or ftype[i]=='SHORT':
            try:
                arcpy.AddField_management(in_table=shp,field_name=flist[i], field_type=ftype[i])
            except:
                print(flist[i]+ ' cannot be created')
        else:
            try:
                arcpy.AddField_management(in_table=shp, field_name=flist[i], field_type=ftype[i], field_length=flen[i])
            except:
                print(flist[i]+' cannot be created')
    print("-fields created-")

def copyfields(shp, oldfield, newfield, ftype):
    flen=len(oldfield)
    for i in range(flen):
        print('copy '+ oldfield[i]+ ' to '+newfield[i])
        if ftype[i]=='FLOAT':
            try:
                fields = [oldfield[i], newfield[i]]
                with arcpy.da.UpdateCursor(shp, fields) as cursor:
                    for row in cursor:
                        row[1] = float(row[0])
                        cursor.updateRow(row)
                del row
                del cursor
            except:
                print(oldfield[i]+' cannot be copied')
        if ftype[i]=='SHORT':
            try:
                fields = [oldfield[i], newfield[i]]
                with arcpy.da.UpdateCursor(shp, fields) as cursor:
                    for row in cursor:
                        row[1] = int(row[0])
                        cursor.updateRow(row)
                del row
                del cursor
            except:
                print(oldfield[i]+' cannot be copied')
        else:
            try:

                fields = [oldfield[i], newfield[i]]
                with arcpy.da.UpdateCursor(shp, fields) as cursor:
                    for row in cursor:
                        row[1] = row[0]
                        cursor.updateRow(row)
                del row
                del cursor
            except:
                print(oldfield[i]+' cannot be copied')
    print("-fields copied-")

def removefields(shp, flist):
    arcpy.DeleteField_management(shp, flist)
    print("-fields deleted-")


def main():
    fcl0=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\CHRP_ClydeRiverA_TreatmentPlan.gdb\PipelineCrossings"

    #planting
    #fcl0 = r"V:\Shared\Ecology\Restoration\FRIAA-2018 CHRP\GIS\shapes\New A\Tree\Tree_planting_final_V4.shp"
    #copy to new fcl
    #planting
    #fcl=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\CHRP_Deliverable.gdb\TreePlanting"

    fcl=r"\\Lacie-5big-pro\gis2\2_FRIAA\Gold Lake_Caribou\Deliverable_1903\CHRP_Deliverable.gdb\PipelineCrossings4"
    if not arcpy.Exists(fcl):
        arcpy.CopyFeatures_management(fcl0,fcl)
    listfieldProp(fcl)
    """
    fieldlist=[]
    fieldtype=[]
    fieldlen=[]
    """


    fieldlist0=['CMPTID','PLNCONT','PLNSUBDATE','CROSS_ID','CROSSREAS','LOCATION','DMS_X','DMS_Y','DD_X','DD_Y','DISP_NUM','DISP_HOLD','DISP_STAT','Notes']

    fieldlist00=['CMPTID','PLNCONT','PLNSUBDATE','CROSS_ID','CROSSREAS','LOCATION','DMS_X','DMS_Y','DD_X','DD_Y',
                 'DISP_NUM','DISP_HOLD','DISP_STAT','Notes','LINE_ID']

    fieldlist1=['Compartment','PlanningContractor','PlanSubmissionDate','CrossingID','CrossingReason','ATSLocation' ,
                'DMS_X','DMS_Y','DD_X','DD_Y','DISP_NUM','DISP_OWNER','DISP_STAT','NOTES']
    tfieldlist=['tCMPTID','tPLNCONT','tPLNSUBDATE','tCROSS_ID','tCROSSREAS','tLOCATION','tDMS_X','tDMS_Y','tDD_X','tDD_Y',
                'DISP_NUM','tDISP_HOLD','tDISP_STAT','tNotes']
    tfieldtype=['TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','FLOAT','FLOAT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT']

    tfieldlen=[30,20,10,10,10,50,20,20,20,20,15,200,70,200]



    if len(tfieldlist):
        addfields(fcl, tfieldlist, tfieldtype, tfieldlen)
        copyfields(fcl, fieldlist0, tfieldlist,tfieldtype)
        removefields(fcl, fieldlist00)
        #new fields
        addfields(fcl, fieldlist1, tfieldtype, tfieldlen)
        copyfields(fcl, tfieldlist, fieldlist1, tfieldtype)
        removefields(fcl,tfieldlist)




if __name__ == "__main__":
    main()
