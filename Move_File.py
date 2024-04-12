import os
import shutil

from_dir = "C:/Users/dell/Downloads"
to_dir = "E:/CODING/Python/Whitehat Jr Projects/Project 111/Document_Files"

list_of_files = os.listdir(from_dir)

# print(list_of_files)

for file in list_of_files:
    root, extension = os.path.splitext(file)