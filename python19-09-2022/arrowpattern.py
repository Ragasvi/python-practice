#arrow shape
x = int(input("enter the number of rows : "))
for i in range(1,x+1):
    print("* "*i)
for i in range(x,0,-1):
    print("* "*i)
    #proper arrow
x = int(input("enter the number of rows : "))
for i in range(1,x+1):
    print("* "*i)
for i in range(x-1,0,-1):
    print("* "*i)
#reverse arrow
x = int(input("enter the number of rows : "))
for i in range(1,x+1):
    print("  " *(x-i)+"* "*i)
for i in range(x-1,0,-1):
    print("  "*(x-i)+"* "*i)
