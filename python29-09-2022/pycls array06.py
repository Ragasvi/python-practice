#array
#write a program to read 'n' integers in an array and read a search element
#and fine the given search element is found or not\

import array
x = array.array('i',[ ])
n = int(input("enter the range:"))
for i in range(n):
    x.append(int(input("enter the elements in array :")))
print(x)
num = int(input("enter the element to search :"))
for i in x:
    if (i == num):
        print("element is found")
        break
if(i != num):
        print("element is not found ")
        
   
        
