# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class complex:
    # a + bi

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def complexnumber(self):
        return f"{self.a}+{self.b}i"

    def __add__(self,x): # add function
        return complex((self.a+x.a),(self.b+x.b))  # it returns integer only, you can create a class  complex so that will be return
        
    def __str__(self):
        return f"{self.a}+{self.b}i"

obj1= complex(4,5)
obj2= complex(5,6)
print(f"{obj1.complexnumber()}\n{obj2.complexnumber()}")
obj3 = obj1+ obj2 # __add__() function you created gets executed
print(obj3) 
print(obj1+obj2) # at first __add__() is run, then when using print function __str__() is runed