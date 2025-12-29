file_path = './File_Handling/demo.txt'

# Reading and Writing files
# file = open('./File_Handling/demo.txt','w+')
# file.write('Hello')
# file.close()

# Write multiple lines
# file = open("./File_Handling/demo.txt","w")

# lines = [
#     "Python is easy\n",
#     "Python is powerful language\n",
#     "Pyhon is used in AI/ML, Data Analytics, Web Development\n"
# ]

# file.writelines(lines)
# file.close()

# Append file content

# file = open('./File_Handling/demo.txt','a')
# lines = [
#     "Python is easy\n",
#     "Python is powerful language\n",
#     "Pyhon is used in AI/ML, Data Analytics, Web Development\n"
# ]
# file.writelines(lines)
# file.close()


# Read and Readlines
# file = open('./File_Handling/demo.txt','r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readable())

# with open('./File_Handling/demo.txt', 'r') as f:
#     while line := f.readline():
#         print(line.strip())

# with open(file_path, "r") as f:
#     for line in f:
#         print(line, end="")

# with open(file_path, 'r') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line.strip())
#             # process line
#     except StopIteration:
#         print("EOF reached")


# with open(file_path, 'r') as f:
#     print(f.readlines())

