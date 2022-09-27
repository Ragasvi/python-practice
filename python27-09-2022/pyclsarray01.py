#arrays
#creation of array using elements
'''import array
x = array.array('i',[10,45,33,89,32])
print(x)
print(type(x))'''
#creating an array using iterator"forloop"
'''import array
x = array.array('i',[10,45,33,89,32])
print(type(x))
for i in x:
    print(i,end =' ')'''
#Append method
#creating an array upto n elements using append method
'''import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter elements :")))
for i in x:
    print(i,end =' ')'''
#create an array using length function len()
'''import array
x = array.array('i',[ ])
n = int(input("enter the range of array :"))
for i in range(n):
    x.append(int(input("enter elements :")))
for i in x:
    print(i,end =' ')
print("\n length of an array is = ",len(x))'''
#index value
import array
x = array.array('i',[10,45,33,89,32])
print(type(x))
print(x[4])
