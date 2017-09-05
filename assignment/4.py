'''Python uses the # character to mark the beginning of a comment. The comment ends at the end of the line containing the # character. In this exercise, you will create a program that removes all of the comments from a Python source file. Check each line in the file to determine if a # character is present. If it is then your program should remove all of the characters from the # character to the end of the line (we’ll ignore the situation where the comment character occurs inside of a string). Save the modified file using a new name that will be entered by the user. The user will also enter the name of the input file. Ensure that an appropriate error message is displayed if a problem is encountered while accessing the files.
'''

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

