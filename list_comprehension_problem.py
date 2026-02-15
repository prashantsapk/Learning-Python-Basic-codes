# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.


# using list comprehension 
a=int(input("Enter the number of which multiplication you want"))
multiplicationtable1=[1,2,3,4,5,6,7,8,9,10]
multiplicationtable2=[a*i for i in  multiplicationtable1 ]
# print(multiplicationtable2)

with (open("Tables.txt","a")as f1):
    f1.write(f"{multiplicationtable2}\n")