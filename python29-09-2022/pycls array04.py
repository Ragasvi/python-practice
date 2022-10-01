#array
#write a program to read  integers in an array and find count number of even
# numbers and odd numbers
import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter an array elements :")))
evencount =0 ; oddcount = 0 #we can give in these ways also ec=0;oc=0/ec=oc=0
for i in x:
    if i % 2 == 0:
        evencount = evencount + 1
    else:
        oddcount = oddcount + 1
print("no of even numbers :",evencount)
print("no of odd numbers :", oddcount)
