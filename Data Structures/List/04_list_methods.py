# enumerate
# Second argument in enumerate function is the starting index
for index, item in enumerate([1,2,3,4,5,6,7,8],1):
    print(f"{item} is in position : {index}")

# iteratior
new_list = ['a','b',1,2,4.5,[3,'hello'],True]
it = iter(new_list)

for _ in range(len(new_list)):
    print(next(it))

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# filter
# filter fucntion is used to filter items from a list, takes function and iterable
# fucntion only return True or False
def check(value):
    if value % 2 == 0 and value % 4 == 0:
        return True

divide_by_two_and_four = list(filter(check,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))

print(divide_by_two_and_four)

# map
# map fucntion return a new list with updated values
def cube(value):
    return pow(value,3)

cube_list = list(map(cube,[2,3,4,5,6,7,8]))
print(cube_list)

# reduce
# reduce fucntion call the fucntion with first two value of the sequence and then result value and next sequence element 
# reduce fucntion return and single value
import functools

def sum(x,y):
    return x + y

added_value = functools.reduce(sum, [2,3,4,5,6,7,8])
print('Added list =', added_value)
