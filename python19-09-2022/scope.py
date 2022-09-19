#LOCAL SCOPE
def jam():
    x = 560
    print(x)
jam()    

#function in side the function
def myfamily():
    n = ("local","global")
    def myinnerfam():
        print(n)
    myinnerfam()
myfamily()    

#GLOBAL SCOPE

x = 300
def myglobal():
    print(x)

myglobal()
print(x)


x = 300
y = 900
def myglobal():
    print(x)

myglobal()
print(x)
print(y)

#global keyword

def myglobal():
    global x
    x = 700

myglobal()
print(x)
