# write a program that the given number is prime or not

number = int(input("enter the value =   "))
if number > 1:
    for i in range(2,number):
        if(number % i) == 0:
            print(number,"it is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")
