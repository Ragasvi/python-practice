#python try except
#exception handling

'''try:
    print(x)
except:
    print("an exception occured")'''

'''x = "Ragasvi"
try:
    print(x)
except:
    print("something went wrong")'''

#many exceptions

'''try:
    print(x)
except NameError:
    print("variable x is not defines")
except:
    print("something else went wrong")'''

#else

'''try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")'''
#when we are not defining a variables    
'''try:
    print(x)
except:
    print("something went wrong")
else:
    print("nothing went wrong")'''

#finally
'''try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")'''
#when we give a variables
'''try:
    print("hello world!")
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")'''
#raise exception
'''x = -1
if x < 0:
    raise Exception("sorry,no numbers below zero")'''
#raise typeerror
x = "good morning"
if not type(x)is int:
    raise TypeError("only intergers are called")
    
