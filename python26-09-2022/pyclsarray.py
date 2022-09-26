#Arrays in python
#syntax
#array name = array(type code,[elements])
import array
a = array.array('i',[1,2,3,4,5])
print(a)

#to know the type
import array
a = array.array('i',[111,23,65,44])
print(type(a))

#for creating we create a typecode

#'i' type array - it indicates positives and negatives numbers'''
import array
a = array.array('i',[1,-7,44,-32,46,111,-123])
print(a)

#'I' -it indicates only positives numbers
import array
a = array.array('I',[23,555,8888,12,45])
print(a)

#to know item size
import array
a = array.array('I',[23,555,8888,12,45])
print(a)
print(a.itemsize)

#float 'f' type array-it indicated integer values as well as decimal values
import array
a = array.array('f',[23,5.55,55,1.4,45])
print(a)

#'b' binary type array - it indicates
#1 byte = -128 to 128 it takes values in between
import array
a = array.array('b',[20,33,56,13])
print(a)

#'B' unsigned integer type array
#1 byte = 0 to 255 it takes in between values
import array
a = array.array('B',[20,33,56,13,34,254])
print(a)

#another syntax for array
from array import *
a = array('b',[20,33,56,13])
print(a)











print(a)
