class Father:
    def __init__(self, salary):
        self.salary = salary

    def display(self):
        print(self.salary)


class Son(Father):
    def __init__(self, salary):
        super().__init__(salary)

    def display(self):
        print(self.salary)

    def __add__(self, other):
        return self.salary + other.salary

a = Son(1000)
# a.display()
b = Father(2000)
print(a + b)

#constuctor overriding