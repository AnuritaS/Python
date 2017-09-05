import sys

file=input("Enter file: \n")
newfile=input("Enter new file: \n")
f=open(file,'r')
try:
    lines=f.readlines()
    f.close()
    try:
        fs=open(newfile,'w')
        for line in lines:
            if('#' not in line):
                fs.write(line)
        fs.close()
    except IOError:
        print("New file opening error")
except IOError:
    print("New file opening error")

