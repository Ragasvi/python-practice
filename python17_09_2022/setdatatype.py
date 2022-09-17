#SET DATATYPE

s=set([1,2,3,4])
print(s)
print(type(s))
#adding elements
s.add("set")
print(s)
# in set we cannot add item to frozen set fs = frozenset([1,2,3,4])
#print(fs)
#fs.add("set")
s1 = set([1,2,3,4])
s2 = set([4,5,6,7])
print(s1.union(s2))
print(s1.difference(s2))
#Operators with set

print(s1 == s2)
print(s1 > s2)
print(23 in s1)
print( 2 in s2)
print(44 not in s1)
print(s1 ^ s2)#exclusive
print(len(s1))
s3 = {"apple","banana","orange"}
s3.update(s1)
print(s3)
for x in s3:
    print(x)
