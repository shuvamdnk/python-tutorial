# Write and Append file ---------------
# file = open("./File_handling/demo.txt","w")
# print(file)
# print(file.closed)
# print(file.mode)
# print(file.name)
# file.write("Hello world")
# lines = [
#     "Hello world\n",
#     "Python is best\n",
#     "Enjoy learning python\n"
# ]
# file.writelines(lines)
# file.close()

# file = open("./File_handling/demo.txt","a")
# file.write("Python is very simple")

# file.write("Python is a powerful language")
# file.close()


# Read file --------------
# file = open("./File_handling/demo.txt","r")

# print(file.read())
# print("First line ",file.readline())
# print("2nd line ",file.readline())
# print("3rd line ",file.readline())
# print("4th line ",file.readline())
# print("5th line ",file.readline())
# print("6th line ",file.readline())


# print(file.readlines())

# print(list(file))
# for line in file:
#     print(line)


# Open file using with keywoed -------------
with open("./File_handling/demo.txt","r") as file:
    lines = list(file)
    for line in lines:
        print(line)

    print(file.closed)

print(file.closed)    