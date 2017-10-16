'''
Given a file name along with fully qualified path, find the inode information of the file.
'''
import os

path = input("Enter the path: ")
print("The inode for it is : ", os.stat(path))