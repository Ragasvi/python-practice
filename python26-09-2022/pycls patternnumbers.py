#write a program to print right angle triangle shape using numbers

rows = int(input("inverted numbers in decreasing order rows = "))
print("==inverted numbers in decreasing order rows==")
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end = ' ')
    print()
#write a program to print triangle shape using numbers
n = int(input("enter no rows :"))
for i in range(n):
    print(" "*(n-i-1),end = "")
    for j in range(i+1):
        print(i+1,"",end = "")
    print()
    print()
