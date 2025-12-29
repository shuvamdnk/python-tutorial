import sys
file_path = './File_Handling/demo.txt'

# with open(sys.argv[1],'r') as f:
#     for line in f:
#         print(line.strip())

# copy a file to another file from command 
with open(sys.argv[2], 'w') as copy_file, open(sys.argv[1] , 'r') as source_file:
    for line in source_file:
        copy_file.write(line.strip())

print("Source file closed ", source_file.closed)
print("Copy file closed ", copy_file.closed)
