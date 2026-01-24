# Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

a =[]
print("Enter the marks for student")
for i in range (1,7,1):
    print(f"Marks for student {i}")
    b=input("Enter the marks")
    a.append(b)

print(f"Maks for student are : {a}")
