import filecmp
import difflib

f1=r'J:\2_SCARI\scari_201806_DidIDFixed.csv'
f2=r'J:\2_SCARI\scari_201806_DidIDFixed2.csv'

fdif=filecmp.cmp(f1,f2)

if fdif:
    print('files are same')
else:
    print('different')
    with open(f1) as file1:
        f1_text=file1.read()
    with open(f2) as file2:
        f2_text=file2.read()

    for line in difflib.unified_diff(f1_text, f2_text, fromfile=f1, tofile=f2, lineterm=''):
        print(line)


print('--end--')