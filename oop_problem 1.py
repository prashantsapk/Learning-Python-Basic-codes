#  Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 

class Calculator:
    def square(self,a):
        print("For calculating the square")
        self.a=a
        self.square=a*a
        print(self.square)

    def cube(self,a):
        print("For calculating the Cube")
        self.a=a
        self.cube=a*a*a
        print(self.cube)

    def squareroot(self,a):
        print("For calculating square root")
        self.a=a
        self.squareroot= a**(1/2)
        print(self.squareroot)

c=Calculator()
inputt = int(input("Enter the number you want"))
b= int(input("Press 1 for square\n2 for cube\n3 for square root"))

if (b==1):
    c.square(inputt)
elif(b==2):
    c.cube(inputt)
else:
    c.squareroot(inputt)