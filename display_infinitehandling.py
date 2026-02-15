# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’

a = int(input("Enter first number"))
b = int(input("Enter first number"))
try:
    print(a/b)
except ZeroDivisionError:
    print("Its zerodivision error you moron")
