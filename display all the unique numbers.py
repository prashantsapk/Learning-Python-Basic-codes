# Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

# we have to use set in this not dictionary

b= set() # created an empty set
for i in range(1,9,1):
    a = int(input("Enter 8 numbers"))
    b.add(a) # add is used, can't use append here

print(b) # unique numbers are printed as sets doesn't store duplicate values