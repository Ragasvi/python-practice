class Student:
    school_name = 'narayana'
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    @classmethod
    def get_grade(cls,name,grade):
        return cls(name,grade)


    def display(self):
        print(self.name + "'s grade is : " + self.grade +' in ' + self.school_name)

s1 = Student('raga','A')
s1.display()
s2 = s1.get_grade('ammu','B')
s2.display()
#s2 = Student.get_grade('pinky','C')
#s2.display()
print(isinstance(s2,Student))