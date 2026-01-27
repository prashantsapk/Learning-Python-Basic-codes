# Write a program to find the sum of first n natural numbers using while loop. 
n = int(input("Enter the number of how many natural number sum you want"))

# should use while loop
# it should be like for example 5, 1 + 2 + 3 + 4 + 5
i =1
j=0

while(i<=n):
   j +=  i
   i+=1
   
print(j)
