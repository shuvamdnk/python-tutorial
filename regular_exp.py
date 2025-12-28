import re
# string = "She sells sea shells on the sea shore"
# pattern1 = 'sells'

# if re.match(pattern=pattern1,string=string, flags=re.IGNORECASE):
#     print("Match Found")
# else:
#     print("Match Not Found")

# if re.search(pattern=pattern1,string=string):
#     print("Search Found")
# else:
#     print("Search Not Found")


# Sub Function 
# name = "Shuvam Dutta shuvam Dutta"

# print(re.sub("Shuvam","Annesha",name, count=2, flags=re.I))

# Findall
# pattern = r"[a-zA-Z]+ \d+"
# matches =  re.findall(pattern,"LXI 2013. VXI 2015")

# for match in matches:
#     print(match)


# FindIter
# pattern = r"[a-zA-Z]+ \d+"
# matches =  re.finditer(pattern,"LXI 2013, VXI 2015")

# for match in matches:
#     # print(match.start())
#     # print(match.end())
#     # print(match.span())
#     print("LXI 2013, VXI 2015"[match.start() : match.end()])


# Flags 
# re.DOTALL
text = """Start
Middle content
End"""

pattern = r"Start.*End"

match_default = re.search(pattern,text,re.S)
print(match_default.group())