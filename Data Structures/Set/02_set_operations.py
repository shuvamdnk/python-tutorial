set1 = set([1,2,3,4,5,6,7,8])
set2 = set([4,5,6,7,8,9,10,11,12])
print("Set1 =",set1)
print("Set2 =",set2)
print("-"*100)
# number exist in both set1 and set2
print(f"Number exist only in both set1 and set2 (Intersection) {set1.intersection(set2)}")

# number exist in set1 or set2 
print(f"Number exist in set1 or set2 (union) {set1.union(set2)}")

# number present in set1 but not set2
print(f"Number present in set1 but not set2 (Difference) {set1.difference(set2)}")

# number present in set2 but not set1
print(f"Number present in set2 but not set1 (Difference) {set2.difference(set1)}")

# number present in either set1 or set2
print(f"Number present in either set1 or set2 (Symmetric Difference) {set1.symmetric_difference(set2)}")