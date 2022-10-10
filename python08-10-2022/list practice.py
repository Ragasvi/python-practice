#list practice
'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.extend('mango')
print(fruits)

fruits.insert(4,'mango')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.index('banana',2))

print(fruits.pop())
print(fruits)
'''
'''
l = [1,2,3]
l[len(l):] = [4]
print(l)
'''
'''
l = [1,2,3,4]
print(l.append(5))
print(l.append(6))
print(l)
print(l.pop())
print(l.pop())
print(l)
'''
'''
from collections import deque

l = deque([1,2,3,4])
l.append(5)
l.append(6)
print(l)
print(l.popleft())
print(l)
print(l.pop())
print(l)

'''
'''
squares = []
for x in range(11):
    squares.append(x**2)
squares.pop()
print(squares)

print(squares)
'''
#squares = [x**2 for x in range(10)]
#print(squares)
'''
l=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            l.append((x,y))
print(l)
'''

#print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])


#l = [1,2,3,4,0,-1,-2,-3,-4]
'''
for x in l:
    print(x*2)
'''
#print([x*2 for x in l])

#filter the list to exculde negative values

#print([x for x in l if x>=0])
'''
for x in l:
    if x>=0:
        print(x)
'''
#apply function to elements
#print([abs(x) for x in l])
'''
for x in l:
    print(abs(x))
'''
#strip()
#flowers = ['  rose  ','  lilly','jasmine    ']
#print([x.strip() for x in flowers])

#creates a 2 tuples in list like (number,square)

#print([(x,x**2) for x in range(10)])

#combining a list
#l = [[1,2,3],[4,5,6],[7,8,9]]
#print([y for x in l for y in x]) 
'''
for x in l:
    for y in x:
        print(y)
'''

#l = [[1,2,3],[4,5,6],[7,8,9],["apple"]]
#print([y for x in l for y in x]) 

#from math import pi
#print([str(round(pi,i)) for i in range(4)])

#del statement
'''
a = [1,2,-44,-67,'apple','mango',4,5,7]
print(a)
del a[0]
print(a)
del a[1:4]
print(a)

del a[:]
print(a)
'''
'''
c = [1,46]
print(c)
del c
'''
#nested list comprehension
'''
matrix = [
    [1,2,3,4],
    [11,12,13,14],
    [21,22,23,23]
]
print(matrix)
#print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))
'''
'''
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            print(list[x,y])

'''
'''
def cricket(score):
    match score:
        case 10:
            return True
        case 20:
            return False
        case _:
            return "wrong"
cricket(10)
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
x = len(matrix)
n = len(transposed)
x == n

transposed = []
for i in range(n):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)












