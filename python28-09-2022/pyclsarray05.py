#array
#write a program to no of positive and negative values in given array
import array
x = array.array('i',[ ])
n = int(input("enter the range:"))
for i in range(n):
    x.append(int(input("enter the elements in array :")))
positivecount = 0 ;negativecount =0 #we can give po=no=0
for i in x:
    if(i>0):
        positivecount = positivecount + 1
    else:
        negativecount = negativecount+1
print("positive count is :", positivecount)
print("negative count is :",negativecount)
