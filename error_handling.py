a = input("Enter number 1")
b = input("Enter number 2")

try:
    print(int(a)+int(b))
except ValueError:
    print("Value error occoured")
else:
    print("This gets executed only if the try was sucessfull")
finally:
    print("it gets executed regardless of error")