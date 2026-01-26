#Write a program to print multiplication table of a given number using while loop
a = int(input("Enter the number of which multiplication table you want"))
i=1
while(i<11):
    print(f"{a} x {i} = {a*i}")
    i+=1