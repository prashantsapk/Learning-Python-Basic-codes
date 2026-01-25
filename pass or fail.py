# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

a =int(input("Enter the marks for Maths"))
b =int(input("Enter the marks for Science"))
c =int(input("Enter the marks for Computer"))

if ((a+b+c)/3>=40):
    print("You passed as your total marks is 40 or above that")
    print(f"Your total marks is{(a+b+c)/3} ")

if(a>=33 and b>=33 and c>=33):
    print("You are passed in all subject")
else:
    print("You failed")


