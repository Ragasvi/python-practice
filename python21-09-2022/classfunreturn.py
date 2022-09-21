# class function return

class course:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_students(self,student):
        self.students.append(student)
    def student_count(self):
        return len(self.students)
#output
c1 = course("python")
c1.add_students("ragasvi")
c1.add_students("ammu")
c1.student_count()
2
