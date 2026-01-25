#multiple if statement

a= int(input("Enter your age"))
if(a==0): #this is independent if
    print("You entered 0")
if (a<18):# here its dependent
    print("your age not eligible to vote")
elif(a>=18):
    print("you can vote")
else:
    print("You entered invalid age")

print("End of the program")