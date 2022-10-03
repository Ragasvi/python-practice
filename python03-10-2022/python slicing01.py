#python slicing
#program to search a substring within a string using slice function

'''s = input("enter a string = ")
sub = input("enter a substring = ")
print(s.find(sub))
ls = len(s)
lsub = len(sub)
if lsub > ls:
    print("invalid substring")
for i in range(0,ls-lsub+1):
    mySlice = slice(i,i+lsub)
    s1 = s[mySlice]
    if s1 == sub:
        print("substring found at position = ", i)
        break
    if s1 != sub:
        print("substring not found")'''


    
s = input("enter a string = ")
sub = input("enter a substring = ")
print(s.find(sub))
ls = len(s)
lsub = len(sub)
if lsub > ls:
    print("invalid substring")
flag =True
for i in range(0,ls-lsub+1):
    mySlice = slice(i,i+lsub)
    s1 = s[mySlice]
    if s1 == sub:
        flag = False
        print("substring found at position = ", i)
        break
if flag:
    print("substring not found")

