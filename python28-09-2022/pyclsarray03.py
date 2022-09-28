#write a program to print sum of elements in an array

import array
x = array.array('i',[ ])
n = int(input("enter the range of an array :"))
for i in range(n):
    x.append(int(input("enter an array elements :")))
sum = 0
for i in x:
    sum = sum+i
print("sum = ",sum)

#write a program to print the smallest element in an array
import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter an array element :")))
smallvalue = 10000
for i in x:
    if i < smallvalue:
        smallvalue = i
print("smallest value is :",smallvalue)

#write a program to print biggest value in array
import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter an array element :")))
bigvalue = 0
for i in x:
    if i > bigvalue:
        bigvalue = i
print("biggest  value is :",bigvalue)

