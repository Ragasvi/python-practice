#multilevel inheritance

class grandfather:
    def birth(self):
        print("iam the base class")
class father(grandfather):
    def born(self):
        print("i have born as derived class")
class son(father):
    def child(self):
        print("i am another dervied class from the father and grandfather class")

p = son()
p.birth()
p.born()
p.child()
    
