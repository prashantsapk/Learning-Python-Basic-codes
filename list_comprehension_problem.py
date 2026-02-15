# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

a = int(input("Enter the number which multiplication table you want"))
list1=[]

for i in range(1,11,1):
    list1.append(a*i)

print(list1)  # normmal way to that using list


# using list comprehension 
multiplicationtable1=[1,2,3,4,5,6,7,8,9,10]
multiplicationtable2=[a*i for i in  multiplicationtable1 ]
print(multiplicationtable2)