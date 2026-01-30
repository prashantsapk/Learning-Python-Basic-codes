#  Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

# program to generate multiplication tables from 2 to 20

file=""

def table(a):
    with open(f"{a}.txt","w") as b:
        for i in range(1,11,1):
            b.write(f"{a} x {i} = {a*i}\n")

# using loop for now 2 to 20 table
for i in range(2,21,1):
    table(i)

# now problem is how to create multiple files, break it and save it
# loop to create multiple files
