#patterns  using without nested loop

#right triangle
x = int(input("enter the number : "))
for i in range(1,x+1):
    print("*" *i)

#square pattern
x = int(input("enter the number of rows : "))
for i in range(x):
    print("*" *x)

#left triangle
x = int(input("enter the number  of rows : "))
for i in range(1,x+1):
    print(" "*(x-i)+"*"*i)

#triangle
x = int(input("enter the number of rows : "))
for i in range(1,x+1):
    print(" "*(x-i)+"* "*i)

#reverse triangle
x = int(input("enter the number of rows : "))   
for i in range(x,0,-1):
    print(" "*(x-i)+"* "*i)


#side triangle
x = int(input("enter the number of rows : "))
for i in range(x,0,-1):
    print("  "*(x-i)+"* "*i)
