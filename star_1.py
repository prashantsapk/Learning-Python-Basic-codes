# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3

n = int(input("Enter the number of lines of pattern you want"))

for i  in range(1,n+1,1):
    print("*"*i,end="") # string gets multiplied, end ="" helps to not to start default new line
    print("\n") # new line or you can just use print("")