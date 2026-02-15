# ENUMERATE FUNCTION IN PYTHON
# The ‘enumerate’ function adds counter to an iterable and returns it
# for i,item in list1:
# print(i,item) # Prints the items of list 1 with index

list1 = [1,2,4,5,6,7]
list2=list1
# for i in list1 :
#  print(i)

for i,item in enumerate(list1) :
    print(i,item) # Prints the items of list 1 with index, here i print index and item prints items


for i,items in enumerate(list2):
    print(i,items)

