#class encapsulation

class car:#base class
    def __init__(self,name,year,speed):
        self.name = name
        self.year = year
        self.speed = speed
        self.__maxspeed()
    def __maxspeed(self):
        print("the maximun speed is 100")
    def getspeed(self):
        print("the getspeed of",self.name,"is:",self.speed)
    def setspeed(self,speed):
        self.speed = speed

a = car('swift',1997,120)
b = car('innova',1998,120)
b.getspeed()
a.getspeed()
a.setspeed(100)
a.getspeed()

class sweden(car):  #child class
    def accelerate(self):
        print("the accelerate speed of ",self.name,"is:",125)
    def opentrunk(self):
        print("truck has been open for",self.name)
c = sweden('i20',2018,120)
c.accelerate()
c.getspeed()
c.setspeed(200)
c.getspeed()

