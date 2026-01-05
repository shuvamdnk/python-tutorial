data = [1,'shuvam',['a','b'],4.5,True]

for item in data:
    if(type(item) == int):
        print("int == ",item)
    # print(type(item) == str)
    elif(type(item) == str):
        print("str == ",item)
    elif(type(item) == list):
        print("list == ",item)
    elif(type(item) == float):
        print("float == ",item)
    elif(type(item) == bool):
        print("bool == ",item)

    if isinstance(item, int):
        print("int (isinstance) == ",item)  
    elif isinstance(item, str):
        print("str (isinstance) == ",item)
    elif isinstance(item, list):
        print("list (isinstance) == ",item)
    elif isinstance(item, float):
        print("float (isinstance) == ",item)
    elif isinstance(item, bool):
        print("bool (isinstance) == ",item)