l1 = [1,2,3,4,5,6,7,8]

# length of list
print("Length of list:", len(l1))

# Contatination of lists
l2 = [9,10,11]
print("Concatenated list:", l2 + l1)

# Repetition of lists
print("Repetition of list:", l1 * 3)

# Check any element in list is false
l3 = [0, False, True]   
print("Any element in l3 is true:", any(l3))

# Check all elements in list are true
print("All elements in l1 are true:", all(l1)) 

# convert touple to list
l4 = list(("Hello", "World"))
print("List converted from string:", l4)

# remove element from list
l1.remove(5)
print("List after removing element 5:", l1)

del l1[2]
print("List after deleting element at index 2:", l1)

l1.pop()
print("List after popping last element:", l1)

# reverse list
new_l1 = list(reversed(l1))
print("Reversed list:", new_l1)

# sort list
l5 = [3,1,4,2,5]    
l5.sort()
print("Sorted list:", l5)

new_l5 = sorted(l5, reverse=True)
print("Sorted list in descending order:", new_l5)

# find index of element
index_of_4 = l5.index(4)
print("Index of element 4 in l5:", index_of_4)

# extend list
l7 = []
l7.extend(l5)
print("Extended list l7 with elements of l5:", l7)