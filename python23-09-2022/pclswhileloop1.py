 #write a program to print natunal numbers upto n

i = 1
n = int(input("enter the value : "))
while i<n:
    print(i,end=" ")
    i +=1
#write a program to print even number upto n

i =2
n= int(input("enter the number :"))
while i<=n:
    print(i, end = " ")
    i+=2

#write a program to print odd number upto n
i = int(input("enter the i value  :"))
n = int(input("enter the n value:"))
while i<=n:
    print(i,end = " ")
    i+=2
#write a program for sum of natural number upto n
i = 1
sum = 0
n = int(input("enter the no:"))
while i<=n:
    sum = sum+i
    i = i+1;
    print("sum = ",sum)

#write a program to print factorial of given number upto n number
i = 1;f = 1
n = int(input("enter the number :"))
while i<=n:
    f=f*i
    i = i+1
    print("fact = ",f)
#write a program to print x^n upto n using while loop
i = 1
p = 1
x = int(input("enter x = "))
n = int(input("enter n = "))
while i<=n:
    p = p*x
    i =i+1
    print("power = ",p)


