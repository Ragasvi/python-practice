#for loop
#write a program to print tables

s = int(input("enter table start number:"))
e = int(input("enter table end number :"))
t = int(input("enter table number :"))
for i in range(s,e):
    r = i*t
    print(i,"x",t,"=",r)

s = int(input("enter table start number:"))
e = int(input("enter table end number :"))
t = int(input("enter table number :"))
for i in range(s,e):
    r = i*t
    print(t,"x",i,"=",r)
