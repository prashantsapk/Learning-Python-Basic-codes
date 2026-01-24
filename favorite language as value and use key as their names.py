# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

b ={} # Empty dictionary

#now need to take favourite language as value & key as name
for i in range(1,5,1):
    a=input("Enter your Name ")
    c=input("Enter the your favourite language")
    b.update({a:c})

print(b)