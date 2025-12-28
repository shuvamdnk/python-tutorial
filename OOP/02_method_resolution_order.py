class A:
    label = "A"

class B(A):
    pass
    # label = "B"

class C(A):
    pass
    # label = "C"

class D(C, B):
    pass

print(D().label)
print(D.__mro__)