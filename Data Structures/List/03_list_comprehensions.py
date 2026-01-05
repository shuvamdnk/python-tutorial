# Cube of number in list
numbers = [1, 2, 3, 4, 5]

cubes = [number**3 for number in numbers]

print(cubes)

# List comprehension with condition

divide_by_two = [i for i in [1,2,3,4,5,6,7,8] if i%2 == 0]

print(divide_by_two)

# using two loops

new_list = [i for i in [2,3,4,5,6] for j in [6,7,8] if i == j]

print(new_list)
