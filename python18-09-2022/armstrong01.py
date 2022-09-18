#armstrong number for a given number
x = int(input("enter the number : "))
num = x
result = 0
n = len(str(x))
while(x!=0):
    digit = x%10
    result = result + digit**n
    x = x//10
if num == result:
    print("given number is a armstrong")
else:
    print("given number is not a armstrong")
