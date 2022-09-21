#inheritance class

class laptop:
    def install(self):
        print("install whatsapp")
class mobile:
    def install(self):
        print("install whatsapp")
    def add(self):
        print("add mobile number")
c = laptop()
c.install()
d = mobile()
d.install()
d.add()
        
class laptop:
    def install(self):
        print("install whatsapp")
class mobile(laptop):
    def add(self):
        print("add mobile number")
c = laptop()
c.install()
d = mobile()
d.install()
d.add()
