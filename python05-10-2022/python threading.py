#threading - it is a sequence of instructions in a program that can run independently
#of remaining process
'''
import threading
def delay():
    print("print after 3 seconds!")
thread = threading.Timer(3,delay)
thread.start()
'''
'''
from threading import *
def show():
    print("this is child thread")
t =Thread(target = show())
t.start()
print("this is parent thread")
'''

from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("\n this is child thread")
t = MyThread()
t.start()
for i in range(5):
    print("\n this is the main thread")
