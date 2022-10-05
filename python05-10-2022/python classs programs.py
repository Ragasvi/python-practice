#program: define a class that can add and subtract two numbers

class add_sub():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        print("the addition of given numbers is :",self.x+self.y)
    def sub(self):
        print("the subtraction of given numbers is :",self.x-self.y)
    def mul(self):
        print("the multiplication of given numbers is :",self.x*self.y)
    def div(self):
        print("the division of given numbers is :",self.x/self.y)

a  = add_sub(100,50)
a.add()
a.sub()
a.mul()
a.div()
       
#for given numbers



class add_sub():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        print("the addition of given numbers is :",self.x+self.y)
    def sub(self):
        print("the subtraction of given numbers is :",self.x-self.y)
    def mul(self):
        print("the multiplication of given numbers is :",self.x*self.y)
    def div(self):
        print("the division of given numbers is :",self.x/self.y)

x = int(input("enter first number: "))
y = int(input("enter second number: "))
a  = add_sub(x,y)
a.add()
a.sub()
a.mul()
a.div()

#program to print the arithmetic operators with choice
class add_sub():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y
x = int(input("enter first number: "))
y = int(input("enter second number: "))
a = add_sub(x,y)
choice = 1
while choice != 0:
    print("0.Exit")
    print("1.Add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    choice = int(input("enter the choice:"))
    if choice == 0:
        print("the code exit")
    if choice == 1:
        print("result:",a.add())
    elif choice == 2:
        print("Result:",a.sub())
    elif choice == 3:
        print("Result:",a.mul())
    elif choice == 4:
        print("Result:",a.div())
    else:
        print("invalid choice")






































