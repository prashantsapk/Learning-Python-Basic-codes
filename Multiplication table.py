# Take input from user and create an multiplication table
a = int(input("Enter the number of which multipliation table you want \t"))
for i in range(1,11,1):
    print(f"{a} x {i} = {a*i}")