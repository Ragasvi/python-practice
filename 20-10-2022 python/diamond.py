class A:
    def __init__(self):
        print('i am A class')
class B(A):
    def __init__(self):
        print('i am B class')
        super(). __init__()
class C(A):
    def __init__(self):
        print('i am C class')
        super(). __init__()
class D(B, C):
    def __init__(self):
        print('i am D class')
        super(). __init__()
#
# s = D()
# #s1 = A()
# #s2 = B()
# #s3 = C()
# print(hash(A()))
#
class A:
    def show(self):
        pass
    def show(self):
        pass
class B:
    def show