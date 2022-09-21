class student:
    def __init__(self,marks,grade):
        self.marks = marks
        self.grade = grade
    @classmethod
    def clsinitialize(cls,marks,grade):
        return(cls(marks+5,grade+ '+'))
    @staticmethod
    def staticinitialize(marks,grade):
        return(student(marks+5,grade+ '+'))

    class Marks(student):
        def display(self):
            print("marks are : (self,marks), grades are :(self,grade)")
    
