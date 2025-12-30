import os
file_path = './File_Handling/demo.txt'

file = open(file_path,'r')
# Get Total Size of the file 
# print(len(file.read()))
print("Initial file pointer position is ",file.tell())

print(file.read(10))
print("After reading file pointer position is ",file.tell())

# seeking file position
print("After setting file pointer position is at 3 ",file.seek(3,1))
print(file.read(10))
print("After reading file pointer position is ",file.tell())

print(os.path.getsize(file_path))