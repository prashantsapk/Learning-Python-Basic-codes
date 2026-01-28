#  Write a program using functions to find greatest of three numbers.
def greatestnum(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the greatest number")
    elif(b>a and b>c):
        print(f"{b} is the greatest number")
    else:
       print(f"{c} is the greatest number")

a = int(input("Enter the number 1"))
b = int(input("Enter the number 2"))
c = int(input("Enter the number 3"))

greatestnum(a,b,c)