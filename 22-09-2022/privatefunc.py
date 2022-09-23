
#private class functions

class Team:
    def __init__(self,name):
        self.__name = name
    def add_members(self,member):
        self.member = member
    def __add_students(self):
        pass

#output
    ============ RESTART: D:\Documents\python practice\private class.py ============
c1 = Team("python")
c1.add_student(joe)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c1.add_student(joe)
AttributeError: 'Team' object has no attribute 'add_student'

