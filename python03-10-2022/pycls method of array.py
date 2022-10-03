#methods of array
#append method
import array
x= array.array('i',[1,2,3,4,5])
print(x)
x.append(int(input("enter the element to be added =")))
print(x)

#count method - to count the given element  how many times are there
import array
a = array.array('i',[34,2,56,33,56,77])
print(a)
c = a.count(56)
print(c)

#extend-to add an array at end of current array
import array
a = array.array('i',[34,67,33,22,66])
print(a)
b = array.array('i',[11,22,33,44,55])
b.extend(a)
print(b)

import array
a = array.array('i',[34,67,33,22,66])
print(a)
b = array.array('i',[11,22,33,44,55])
a.extend(b)
print(a)

#fromlist method
import array
l1 = [10,20,30,40,50]
print(type(list))
x = array.array('i',[33,44,55,66])
x.fromlist(l1)
print(x)

#fromstring method
'''import array
str = 'good evening'
a = array.array('i',[1,2,3,4,5])
a.fromstring(str)
print(a)'''

#index method
import array
x = array.array('i',[33,55,66,77,88,99,333,222,222])
a=x.index(222)
print(a)
#insert method
import array
a = array.array('i',[10,20,30,40,50,60])
a.insert(7,70)
print("the insert element is ",a)
#pop method

import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.pop(3)
print(a)

#pop method without index number
import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.pop()
print(a)

'''import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.pop(7)
print(a)'''

#remove method
import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.remove(99)
print(a)

'''import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.remove()
print(a)'''

#reverse method
import array
a = array.array('i',[33,99,88,66,55])
print(a)
a.reverse()
print(a)
#tolist method
import array
a = array.array('i',[33,99,88,66,55])
print(a)
l1 = a.tolist()
print(l1)

#typecode or attribute
import array
a = array.array('B',[33,99,88,66,55])
print(a)
print(a.typecode)
#itemsize attribute
import array
a = array.array('b',[33,99,88,66,55])
print(a)
print(a.itemsize)

#sorting method
import array
a = array.array('i',[33,99,88,66,55])
print(a)
b = sorted(a)
print(b)

#sorting in decending order

import array
a = array.array('i',[33,99,88,66,55])
print(a)
b = sorted(a,reverse = True)
print(b)

import array
a = array.array('i',[33,99,88,66,55])
print(a)
b = sorted(a,reverse = False)
print(b)
































