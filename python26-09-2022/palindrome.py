#palindrome

'''def ispalindrome(s):
    return s == s
s = input("enter the word for palindrome : ")
n = ispalindrome(s)
if n:
    print("yes")
else:
    print("no")'''


x = input("enter the palindrome word :")
w = ''
for i in x:
    w = i+w
if(x==w):
    print("given word is palindrome")
else:
    print("given word is not a palindrome")
