#write a program to print reverse loop using for loop

for i in range(10,0,-1):
    print(i)

s = int(input("enter the start value :"))
e = int(input("enter the end value :"))
st = int(input("enter step value :"))
for i in range(s,e,st):
    print(i)
