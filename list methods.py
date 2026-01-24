a = [6,"Prashant","apple","Mango", 5]
print("Printing the list",a)
a.append("Ram")
print("List after appending Ram",a)
print("Accessing the list, 1 element i.e.",a[1])
print("current list",a)

b=[2,8,4,9,3,1]
print("Number list",b)
b.sort()
print("Number list after using sort",b)
b.reverse()
print("List after using reverse",b)

# pop insert & remove
print("the list is",b)
b.insert(1,"ram")
print("After using insert in 1 element",b)

print("The current list is ",b)
b.remove("ram")
print("After using remove ram",b)

print("The current list is ",b)
b.pop(1)
print("After using pop on element 1",b)