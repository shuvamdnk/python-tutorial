import os
from pathlib import Path
file_path = './File_Handling/demo2.txt'

if(os.path.exists(file_path)):
    os.remove(file_path)

print("File removed")


print(os.getcwd())
print(os.listdir())