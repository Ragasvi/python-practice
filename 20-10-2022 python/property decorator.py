#property : it allows us to use method as attribute




# class animal:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#         self.msg = self.name +' is a type of '+ self.type +' animal'
#
#
# a = animal('tiger','wild')
# print(a.name)
# print(a.type)
# print(a.msg)
# a.name = 'dog'
# a.type = 'domestic'
# print(a.name)
# print(a.type)
# print(a.msg)


# class animal:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#     def msg(self):
#         return  self.name +' is a type of '+ self.type +' animal'
#
# a = animal('tiger','wild')
# print(a.name)
# print(a.type)
# print(a.msg())
# a.name = 'dog'
# a.type = 'domestic'
# print(a.name)
# print(a.type)
# print(a.msg())

#
# class animal:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#     @property
#     def msg(self):
#         return  self.name +' is a type of '+ self.type +' animal'
#
# a = animal('tiger','wild')
# print(a.name)
# print(a.type)
# print(a.msg)
# a.name = 'dog'
# a.type = 'domestic'
# print(a.name)
# print(a.type)
# print(a.msg)

# class student:
#     def __init__(self,marks):
#         self.marks = marks
#     def per(self):
#         return (self.marks/600)*100
#
# s = student(300)
# print(s.per())
#s.marks = 400
#print(s.per())




# class student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def per(self):
#         return (self.__marks/600)*100
#     def setter(self,value):
#         self.__marks = value
#     def getter(self):
#         return self.__marks
#
#
# s = student(300)
# s.setter(500)
# print(s.getter())
# print(s.per(),'%')
#
# class student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def per(self):
#         return (self.__marks/600)*100
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,value):
#         self.__marks = value
#
#
#
# s = student(300)
# s.marks =500
# print(s.marks)
# print(s.per(),'%')
# s.marks = 200
# print(s.marks)
# print(s.per(),'%')
#


# class student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def per(self):
#         return (self.__marks/600)*100
#
#     def display(self):
#         return self.__marks
#
#     def show(self,value):
#         self.__marks = value
#     marks = property(display,show)
#
# s = student(300)
# s.marks =500
# print(s.marks)
# print(s.per(),'%')
# s.marks = 200
# print(s.marks)
# print(s.per(),'%')

#class method
class student:
    school = 'narayana'
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        student.school = 'high school'
    def msg(self):
        print(self.name+ ' got ' + self.marks,'%')
    @classmethod
    def sch(cls):
        print('school name has changed')
s = student('ragasvi','500')
s.msg()
print(s.school)
print(student.school)
student.sch()
s.sch()
