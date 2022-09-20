#PYTHON ARRAY
from array import*
array_num = array('i',[1,3,5,7,9])
for i in array_num:
    print(i)
print("access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])
#appending
array_num.append(11)
print(array_num)
#Reverse
num= array('i',[1,3,5,3,7,1,9,3])
num.reverse()
print("reverse of the original array")
print(num)
#item size
print(str(num))
print(str(num.itemsize))
#bufferinfo and memory buffer in python
print(str(num.buffer_info()))
print("size of memory buffer in bytes :"+str(num.buffer_info()*num.itemsize))
print("size of memory buffer in bytes :"+str(num.buffer_info()[1]*num.itemsize))
#append items from a list
print(str(array_num))
n = [11,22,33,44]
print(str(num))
array_num.fromlist(n)
print(str(array_num))
#extend
print(str(array_num))
array_num.extend(array_num)
print(str(array_num))
#insert new element in middle of array
x= ["python","java"]
x.insert(1,"oracle")
print(x)
#remove a specified element 
num.pop(3)
print(num)
