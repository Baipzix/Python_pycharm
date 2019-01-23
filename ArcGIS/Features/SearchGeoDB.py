import arcpy
import os, glob

from datetime import datetime

def shp_size(file):
    size_in_total=sum([os.stat(x).st_size for x in glob.glob(file.split(".")[0]+"*")])
    return size_in_total

def m_time(file):
    dt=[None]*2
    docinfo=os.stat(file)

    dt[0]=datetime.fromtimestamp(docinfo.st_ctime)
    dt[1]=datetime.fromtimestamp(docinfo.st_mtime)
    return dt

def FileInfo(dir):
    infoList = []
    for root, subs, files in os.walk(dir):
        print(root)
        arcpy.env.workspace=root

        for file in files:
            if file.endswith(".shp"):
                file_info = []
                shp = os.path.join(root, file)


                shpsize = shp_size(shp)
                fdate = m_time(shp)

                try:
                    desc = arcpy.Describe(shp)
                    rowNumber = arcpy.GetCount_management(shp)
                    featureType=desc.featureType
                    shapeType=desc.shapeType
                except Exception:
                    featureType="invalid"
                    shapeType="invalid"
                    rowNumber=None

                file_info.append(file)
                file_info.append(root)
                file_info.append(shpsize)
                file_info.append(str(fdate[0]))
                file_info.append(str(fdate[1]))
                file_info.append(featureType)
                file_info.append(shapeType)
                file_info.append(rowNumber)

                infoList.append(file_info)
    return infoList


def WriteToFile(file, dat):
    if not os.path.isfile(file):
        head = ['name', 'directory', 'size', 'create time', 'last modified', 'feature type', 'shape type',
                'feature number']
        f=open(file, "w+")
        for item in head:
            f.write(str(item)+',')
        f.write('\n')
    else:
        f=open(file,"a")
    #dat=join(dat)

    for row in dat:
        for item in row:
            f.write(str(item)+',')
        f.write('\n')
    f.close()



def main():

    #dirs = [r"C:/", r"E:/", r"/LACIE-5BIG-PRO"]
    flist = []
    docname=r"C:\Users\haitaol\Documents\Projects\SOP\GeoDBList.txt"

    netname = [r"\\Lacie-5big-pro"]
    dirname=["admin", "aesrd","ap","ates","Cenovus","dcc","fc","fgya","Fieldstaff",
     "gis","gis2","hwp","Lakeland","ls","meg","memss","Move_To_Backup","mwfp",
     "ne","oe","Public","sc","sculc","slp","tec","ti","TimeSheet","tsh","Ualberta","vc","wc","wm"]
    dirlist=[netname[0]+"\\"+x for x in dirname]
    dirlist.append(r"V:/")

    for dir in dirlist:
        info=FileInfo(dir)
        flist.extend(info)

    #write to txt
    WriteToFile(docname, flist)
    print(len(flist))
    print("---END---")


if __name__ == "__main__":
    start_time=datetime.now()
    main()
    print(datetime.now()-start_time)
