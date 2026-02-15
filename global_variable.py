# its for global variable

a = 1
b=3
c=5
def printfunction():
    print(a) # prints global variable
    b=2
    print(b) # prints local variable as its inside the function
    global c# so this shit changes global variable c
    c=c+4 # global variable = 5+4 = 9

printfunction() # if this function is called then only global variable is changed for c.
print(c) # it prints 9, i.e the changed global variable