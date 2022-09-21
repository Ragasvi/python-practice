#class fields
class student:
    clg = "narayana jr clg"
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print("student name:",self.name)
        print("student rollno:",self.rollno)
        print("student clg:",self.clg)
student("ragasvi","1001").display()
student("saritha","1002").display()
#staticmethod
class person:
    @staticmethod
    def display():
        print("heyyy")
p = person()
p.display()        
