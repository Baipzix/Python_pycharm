import arcpy
import os, glob
from laspy import file
from datetime import datetime
import sys


def shp_size(infile):
    size_in_total = sum([os.stat(x).st_size for x in glob.glob(infile.split(".")[0] + "*")])
    return size_in_total


def m_time(infile):
    dt = [None] * 2
    docinfo = os.stat(infile)

    dt[0] = datetime.fromtimestamp(docinfo.st_ctime)
    dt[1] = datetime.fromtimestamp(docinfo.st_mtime)
    return dt


def read_las(lasfile):
    try:
        f = file.File(lasfile, mode='r')

        infolist = []
        h = f.header
        infolist.extend(h.max)
        infolist.extend(h.min)
        infolist.append(h.point_records_count)
        infolist.extend(h.point_return_count)
        f.close()
    except IOError as e:
        print("I/O error({0}):{1}".format(e.errno,e.strerror))
        infolist = [None] * 12
    except:
        print("unexpected error", sys.exc_info())
        print("Cannot open file: " + lasfile)
        infolist = [None] * 12

    return infolist


def fileInfo(filedir):
    infoList = []
    for root, subs, files in os.walk(filedir):
        print(root)

        for infile in files:
            if infile.endswith(".las"):
                file_info = []
                las = os.path.join(root, infile)

                lassize = os.stat(las).st_size

                fdate = m_time(las)

                lasInfo = read_las(las)

                file_info.append(infile)
                file_info.append(root)
                file_info.append(lassize)
                file_info.append(str(fdate[0]))
                file_info.append(str(fdate[1]))
                file_info.extend(lasInfo)

                infoList.append(file_info)
    return infoList


def writeToFile(infile, dat):
    if not os.path.isfile(infile):
        head = ['name', 'directory', 'size', 'create time', 'last modified',
                'max_x', 'max_y', 'max_z', 'min_x', 'min_y', 'min_z', 'point_record',
                'return1', 'return2', 'return3', 'return4', 'return5']
        f = open(infile, "w+")
        for item in head:
            f.write(str(item) + ',')
        f.write('\n')
    else:
        f = open(infile, "a")

    for row in dat:
        for item in row:
            f.write(str(item) + ',')
        f.write('\n')
    f.close()


def main():
    dirlist = [r"C:/", r"E:/", r"V:/"]
    flist = []
    docname = r"C:\Users\haitaol\Documents\Projects\SOP\LiDARList.txt"
    netname = r"\\Lacie-5big-pro"
    dirname = ["admin", "aesrd", "ap", "ates", "Cenovus", "dcc", "fc", "fgya", "Fieldstaff",
               "gis", "gis2", "hwp", "Lakeland", "ls", "meg", "memss", "Move_To_Backup", "mwfp",
               "ne", "oe", "Public", "sc", "sculc", "slp", "tec", "ti", "TimeSheet", "tsh", "Ualberta", "vc", "wc",
               "wm"]

    vdir = [netname + "\\" + x for x in dirname]
    dirlist.extend(vdir)

    for dirs in dirlist:
        info = fileInfo(dirs)
        if len(info) > 0:
            flist.extend(info)

    # write to txt
    writeToFile(docname, flist)
    print(len(flist))
    print("---END---")


if __name__ == "__main__":
    start_time = datetime.now()
    main()
    print(datetime.now())
    print(datetime.now() - start_time)
