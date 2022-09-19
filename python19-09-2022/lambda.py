#lambda function


x = lambda a,b : a+b
print(x(3,4))


x = lambda a,b,c : a+b+c
print(x(3,4,9))


x = lambda a,b,c,d : a + b + c + d
print(x(3,4,9,12))



x = lambda a,b,c,d : a + b - c / d
print(x(3,4,9,12))


def myfunction(n):
    return lambda b : b*n
b = myfunction(2)
print(b(11))


def myfunction(n):
    return lambda b : b*n
myfunc = myfunction(2)
mynum = myfunction(3)
print(myfunc(11))
print(mynum(11))



def myfunction(n):
    return lambda b : b*n
c = myfunction(2)
a = myfunction(3)
print(c(11))
print(a(11))
