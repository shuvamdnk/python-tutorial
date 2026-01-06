# "*" is known as gather
def display(*args):
    print(args)

tup = (1,2,3,4,5,6,7,8)
display(tup)

# scatter
display(*tup)

# zip()
lst = ['a','b','c','d','e']

print(list(zip(tup,lst,'hello',{2423,2342,4422,5323})))
