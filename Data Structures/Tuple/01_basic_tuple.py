# Creating tuple
# Tuple is immutable
t1 = (2,)
print(type(t1))

# , is important otherwise it will be int data type

# other way to assign tuple
t2 = 2,3,4,5,6,7,8
t3 = tuple()

# divmod return tuple
print(divmod(28,5))

print(t2[-3:-6:-1])

# tuple Assignment
(v1, v2, v3) = (1,2,3)
print(v1, v2, v3)