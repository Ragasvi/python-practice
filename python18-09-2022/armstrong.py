# ARMSTRONG NUMBER: if the sum of nth power of each digit equals to number that is armstrong number



#if we want a armstrong number ifrom 1-100

for x in range(201):
    num = x
    result = 0
    n = len(str(x))
    while(x!=0):
        digit = x%10
        result = result + digit**n
        x = x//10
    if num == result:
        print(num)
   
