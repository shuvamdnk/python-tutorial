import os
file_path = './File_Handling/demo.txt'
print(os.stat(file_path).st_mode)