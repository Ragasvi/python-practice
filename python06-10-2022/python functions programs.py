#functions
#write a program to print  that calculates the squares of numbers ranging from
#given number using user defines function
'''
def square(a):
    return a*a
n = int(input("enter the range value:"))
for i in range(0,n):
    print(square(i))
'''

#write a program that can multiply all the numbers in a list using
#inbuilt function
   
def multiply(*num):
    total = 1
    for i in num:
        total = total*i
    return total
result = multiply(2,6,3,4,6,2,1)
print("the multiplication of given numbers is :",result)

