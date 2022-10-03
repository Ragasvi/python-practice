#slicing
#syn - object(start:stop:step)
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = tuple(l1)
print(l1)
print(l2)
#start (slicing the one value)
print('0 =',l1[0])
print('5 =',l1[5])
print('-3 =',l1[-3])
print('-9 =',l1[-9])
print('-10 =',l1[-10])
print('-1 =',l1[-1])
print(l1[len(l1)-1])
#stop(slicing two values)
print('[1:3] = ',l1[1:3])
print('[1:10]=',l1[1:10])
print('[0:11] = ',l1[0:11])
print('[0:-6] =',l1[0:-6])
print('[-1:-10] =',l1[-1:-10])
print('[0:-11] =',l1[0:-11])
print('[0:10] =',l1[0:10])
print('[0:-1] =',l1[0:-1])
#step
print('[::3] =',l1[::3])
print('[::2] =',l1[::2])
print('[::-3] =',l1[::-3])
print('[-3::-3] =',l1[-3::-3])
print('l2[::3] =',l2[::3])
#slicing with string
python = "python is a programming language"
print(python[0])
print('python[-1] =',python[-1])
print('python[::-1] =',python[::-1])
print('python[10] =',python[10:])
print('python[-12] =',python[-12:])
#calling a slice
mySlice = slice(0,9,2)
print(l1)
print('the list after we called',l1[mySlice])
print(python)
print("the string in slice object =",python[mySlice])












