import os
import shutil
from_dir = r"C:\Users\dassu\Downloads\C 103"
to_dir = r"C:\Users\dassu\OneDrive\Desktop\WhitehatJr"
listOfFiles = os.listdir(from_dir)
print(listOfFiles)

for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)