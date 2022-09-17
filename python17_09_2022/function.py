#FUNCTION CREATING AND CALLING
def my_function():
    print("hello from  a function")
my_function()
#passing arguments in function
def func(name):
    print(name)
func("ragasvi")
func("apple")
def fun(name):
    print(name  +  " month ")
fun("september")
fun("april")
#in function we have to call correct number of
#arguments not more or not less
#keyword arguments
def family(child1,child2,child3):
    print("the youngest child is " + child2)
family(child1 = "mango",child2 = "apple",child3 = "banana")
#arbitary arguments
def fam(*child):
    print("the oldest child is " +child[1])
fam("perk","silk","munch")    
#arbitary arguments **kwargs
def name(**name):
    print("her last name is " + name["lname"])
name(fname = "ragasvi",lname = "maruri")    
#default parameter value
def country(country = "norway"):
    print("i am from " + country)
country("sweden")
country("india")
country("london")
country()

#passing a list as an argument

def function(fruits):
    for x in fruits:
        print(x)
fruits = ["papaya","dragon","cherry"]
function(fruits)
