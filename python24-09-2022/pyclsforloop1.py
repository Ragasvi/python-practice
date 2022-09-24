#for loop
#write a program to print numbers using range() function

#syntax : range(initial value,final valueor end value,step value
for i in range(5,11):
    print(i)

for i in range(4,34,3):
    print (i)

#write a program to print sequence of element using for loop
s = int(input("enter the start value :"))
e = int(input("enter the end value :"))
st = int(input("enter step value :"))
for i in range(s,e,st):
    print(i)

s = int(input("enter the start value :"))
e = int(input("enter the end value :"))
st = int(input("enter step value :"))
for i in range(s,e+1,st):
    print(i)
