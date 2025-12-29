# Read a file
# default mode is 'read'
# file = open('./File_Handling/demo.txt')
# print(file.mode)

file = open('./File_Handling/demo.txt','wb')
print(file.closed)

file.close()

print(file.closed)