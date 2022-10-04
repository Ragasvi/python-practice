#class inheritance
class car:  #base class
    def __init__(self,name,year,speed):
        self.name = name
        self.year = year
        self.speed = speed
    def maxspeed(self):
        print("the maximun speed of",self.name,"is:",self.speed)
    def setspeed(self,speed):
        self.speed = speed
        
a = car('audi',2019,180)
a.maxspeed()
b = car('bmw',2009,200)
b.maxspeed()
b.setspeed(130)
b.maxspeed()

class sweden(car):  #child class
    def accelerate(self):
        print("the accelerate speed of ",self.name,"is:",125)
    def opentrunk(self):
        print("truck has been open for",self.name)
class SUV(car):  #child class
    def accelerate(self):
        print("the accelerate speed of ",self.name,"is:",135)
c = sweden('honda',1998,145)
c.accelerate()
c.opentrunk()
#a.opentrunk()
a = sweden('audi',2019,180)
a.accelerate()
a.opentrunk()
a = SUV('audi',2019,180)
a.accelerate()
#c.getspeed()
#c.setspeed(210)
#c.getspeed()

