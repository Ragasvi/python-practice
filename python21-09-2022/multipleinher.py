#multiple inheritance

class wateranimal:
    def printing(self):
        print("the animal will be in water")
class landanimal:
    def display(self):
        print("the animal will be on land")
class crocodile(wateranimal,landanimal):
    pass
p=crocodile()
p.printing()
p.display()
