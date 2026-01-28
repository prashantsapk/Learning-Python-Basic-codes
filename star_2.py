# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 

# another example
#* * *
#*   *
#* * *
#* * *
#*   *
#* * *


n= int(input("Enter the number you want"))
for i in range(1,n+1,1):
    if (i%2==0):
        print("*   "*2) # build a logic here now
    else:
        print("* "*3)

    # do it on your own use your logic , if you can't do this quit coding