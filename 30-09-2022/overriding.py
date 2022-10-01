#method overriding

class vegetables:
    def display(self):
        print("the items belongs to class vegetables")
class leafyvegetables(vegetables):
    pass
    
a = leafyvegetables()
a.display()

#this is an example of method overriding
class fruits:
    def display(self):
        print("the items belongs to class fruits")
class vegetables(fruits):
    def display(self):
        print("this item belong to class leafyvegetables")

a = vegetables()
a.display()
