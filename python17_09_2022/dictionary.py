# DICTIONARY DATATYPE
d1={}
print(d1)
print(type(d1))
d2 = {1:"ragasvi",2:"python",3:"language"}
print(d2)
d3 = {"name" : "ragasvi","age" : 24, "profession" : "worker"}
print(d3)
#nested dictionary
d4 = {"name" : {"fname" : "ragasvi"},"age" :24}
print(d4)
#adding element
d1[0] = "welcome"
print(d1)
d1["name"] = "apple"
print(d1)
d1[1] = ("how ","are" ,"you")
print(d1)
# updating the elements in dictionary
d1["name"] = {"fname" : "apple","last" : "mango"}
print(d1)
#acessing the elements
print(d1["name"])
print(d1["name"]["last"])
print(d1.get(0))
#deleting elements
d1.pop(0)
print(d1)
d2.popitem()#as the pop item deletes the last item in dic
print(d2)
d1.values()
print(d1)

#keys = {'a','b','c','d'}
#value = 1
#dict.fromkeys(keys,value)

d2.clear()
print(d2)

