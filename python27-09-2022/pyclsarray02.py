#array
#print an reverse array of  elements using while loop in index model
import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter the elements : ")))
l = len(x)
i = l-1
while i>=0:
    print(x[i],end = ' ')
    i-=1
#print an reverse array of elements using for loop
import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter the elements : ")))
l = len(x)
for a in range(l-1,-1,-1):
    print(x[a],end = ' ')
