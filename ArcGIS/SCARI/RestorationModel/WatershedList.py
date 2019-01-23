import arcpy
import csv
import pandas as pd
import numpy as np


class Cross():
    crsCount = 0

    def __init__(self, id, parents, children):
        self.id = id
        self.parents = parents
        self.children = children
        Cross.crsCount += 1

    def listParents(self):
        print("Parent watershed/crossing Id:", self.parents)

    def listChildren(self):
        print("Child watershed/crossing ID:", self.children)

    def totalCross(self):
        print("Total crossings: %d" % Cross.crsCount)


def watershed_parent(crsid, crslist):
    w_p = []
    for crs in crslist:
        if crsid in crs.children:
            w_p.append(crs.id)
    return w_p

# select crossing inside the watershed
def SelectChildCrossing(watershd, crs, fieldname):
    crslist = []
    arcpy.MakeFeatureLayer_management(crs, 'crossing')
    arcpy.MakeFeatureLayer_management(watershd, 'watershed')

    whereClause = ''' "GRIDCODE"= {} '''.format(fieldname)

    arcpy.SelectLayerByAttribute_management("watershed", "NEW_SELECTION", whereClause)
    arcpy.SelectLayerByLocation_management(in_layer='crossing', overlap_type='COMPLETELY_WITHIN',
                                                             select_features='watershed')
    rows = arcpy.SearchCursor('crossing')

    for rw in rows:
        crslist.append(rw.getValue('grid_code'))
    del rw
    del rows

    # print(len(crslist))
    #print('all child crossing',crslist)
    arcpy.Delete_management('crossing')
    arcpy.Delete_management('watershed')

    crslist=list(set(crslist))
    maincross=crslist.index(fieldname)
    crslist.pop(maincross)
    return crslist


def savetocsv(objlist):
    clm = ['id', 'Parents', 'Children']
    df0 = pd.DataFrame(columns=clm)

    for crs in objlist:
        plen = len(crs.parents)
        clen = len(crs.children)

        if plen >= clen and plen > 0:
            dflen = plen
        elif plen < clen:
            dflen = clen
        elif plen == clen and plen == 0:
            dflen = 1

        dt = np.array([np.arange(dflen)] * 3).T
        df = pd.DataFrame(dt, columns=clm)

        df['id'] = crs.id

        if plen == clen:
            if plen==0:
                df['Parents']=np.nan
                df['Children']=np.nan
            else:
                df['Parents'] = crs.parents
                df['Children'] = crs.children
        elif plen > clen:
            df['Parents'] = crs.parents
            pcdif = plen - clen
            applist = np.empty(pcdif)
            applist[:] = np.nan
            tmplist = crs.children
            tmplist = tmplist.append(applist)
            df['Children'] = tmplist
        elif plen < clen:
            df['Children'] = crs.children
            pcdif = clen - plen
            applist = np.empty(pcdif)
            applist[:] = np.nan
            tmplist = crs.parents
            tmplist = tmplist.append(applist)
            df['Parents']=tmplist

        df0 = df0.append(df)
        df0.to_csv(r'J:\2_SCARI\SwanHill_Restoration_Model\watershed_pc2.csv')






def main():
    WatershedShapefile = r'\\Lacie-5big-pro\gis2\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\crossingwatershed\watershed_crossing_cln.shp'
    Crossings = r'\\Lacie-5big-pro\gis2\2_SCARI\SwanHill_Restoration_Model\WatershedModel2\SwanHill.gdb\snappoint25'
    # search for all watershed
    #    # field use to search watershed
    field = 'GRIDCODE'
    crsObjlist = []
    cursor = arcpy.SearchCursor(WatershedShapefile, fields='GRIDCODE')
    i = 0
    for row in cursor:
        fieldname = row.getValue(field)
        parentlist = []
        crslist = SelectChildCrossing(WatershedShapefile, Crossings, fieldname)
        i = Cross(fieldname, parentlist, crslist)
        crsObjlist.append(i)
    del row
    del cursor

    for obji in crsObjlist:
        obji.parents=watershed_parent(obji.id, crsObjlist)

    objatt=[]
    for obj in crsObjlist:
        att=[]
        att.append(obj.id)
        att.append(obj.parents)
        att.append(obj.children)

        print(att)
        objatt.extend(att)

    savetocsv(crsObjlist)


    with open(r'J:\2_SCARI\SwanHill_Restoration_Model\watershedlist2.txt', 'w') as csvfile:
        for att in objatt:
            print >> csvfile, att




if __name__ == "__main__":
    main()
