import re
import os
files=os.lisdir()
print(files)
flag=0
for item in files:
    match=re.match(r"[A-Z_a-z0-9]+.py$",item)
    if match:
        if(flag==0):
            c_size=os.path.getsize(item)
            large=c_size
            flag=flag+1
        c_size=os.path.getsize(item)
        large=max(large,c_size)
        if large==c_size:
           large_file=item
    else:
        print("not python file")
    
#busy_days.py","date_month.py","last_name_sort.py"]
print("Largest file is: ",large_file)
'''for file in list_files:
    with open(file,mode="r") as files:
        files.read()
        s=files.tell()
        file_size[int(s)]=file'''
        
'''largest= max(file_size.keys())
print(file_size)
print("Largest file is: ",file_size[largest])'''
