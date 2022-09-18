# REGULAR EXPRESSION
#check if the strings starts with "the" and ends with "spain"
import re
txt = "the rain in spain"
x = re.search("^the.*spain$",txt)
if x:
    print("YES! we have a match!")
else:
    print("no match")

# Return a list containing every occurrence of "in"
x = re.findall("in",txt)
print(x)
x = re.findall("london",txt)
print(x)
if(x):
    print("yes,there is a least one match!")
else:
    print("no match")
#find the white spaces
txt = "hello good morning everyone there"    
x = re.search("\s",txt)
print("the first white-space character is located in positions:", x.start())
#check if the string starts with "at"
x = re.findall("\Aat",txt)
print(x)
if x:
    print("yes, there is a match!")
else:
    print("no match")
#check is string contains any digits
x = re.findall("\d", txt)
print(x)
if x:
    print("yes")
else:
    print("no match")
#split the string at every white space character
txt = "hello good morning everyone there"    
x = re.split("\s",txt)
print(x)
# replace all white spaces characters with the digit 4

x = re.sub("\s","4",txt)
print(x)
