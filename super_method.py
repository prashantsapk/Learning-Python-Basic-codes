# super

class employee:
    def __init__(self):
        print("Hello world") # prints the constructor
    a=1

class programmer(employee):
    def __init__(self):
        print("Child constructor")
        super().__init__() # this will run the parent constructor as well

b=programmer()
print(b.a)