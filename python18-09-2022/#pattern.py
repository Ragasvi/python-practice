#PATTERNS
#to print "*" pattern in square
x= int(input("enter the number of * to be printed : "))
for i in range(x):
    for j in range(x):
        print("*",end = "")
    print()    
# print * in right angle triangle
x = int(input("enter the number of * to be printed :"))
for i in range(x):
    for j in range(i+1):
        print("*",end="")
    print()    
#print * in reverse right angle triangle
x = int(input("enter the number  : "))
for i in range(x):
    for j in range(x-i):
        print("*",end="")
    print()
#print the * in triangle
x = int(input("enter the number :"))
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end = " ")
    print()
#print right triangle mirror image
x = int(input("enter the number :"))
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end ="")
    print()    

