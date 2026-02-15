# LIST COMPREHENSIONS
# List Comprehension is an elegant way to create lists based on existing lists.
# list1 = [1,7,12,11,22,]
# list2 = [i for item in list 1 if item > 8]


list1 = [4,5,6,7]
# emptylist=[]


# for i in list1:
#     emptylist.append(i*i) # for only indexing we use[], else we use ()

# for i in emptylist:
#     print(i)

# the same stuffs can be done simply by

list2=[i*i for i in list1]
print(list2)

