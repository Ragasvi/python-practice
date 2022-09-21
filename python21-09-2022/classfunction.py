#class function
class course:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_students(self,student):
        self.students.append(student)
        

c1 = course("python")
c1.add_students("john")
c1.add_students("peter")
c1.students

  
