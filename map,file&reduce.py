# MAP, FILTER & REDUCE
# Map applies a function to all the items in an input_list.
# Syntax.
# map(function, input_list)
# # the function can be lambda function
# Filter creates a list of items for which the function returns true.
# list(filter(function))
# # the function can be lambda function
# Reduce applies a rolling computation to sequential pair of elements.
# from functools import reduce
# val=reduce (function, list1)
# # the function can be lambda function


# map function, map(function, input_list)
list1=(1,3,5,6)
a= lambda b: b*b

b = map(a,list1)
print(tuple(b))


# filer function
# Filter creates a list of items for which the function returns true.
# list(filter(function))

def even(n):
    if (n%2==0):
        return True
    return False

onlyeven = filter(even,list1)
print(list(onlyeven))

# reduce # it pplies a rolling computation to sequential pair of elements.
# its same like factorial problem you faced, like 4! = 1*2*3*4
#now it will be like 2*3*4 then aftee it performs 2 x3 it will be 6 x 4 then it does again, like this it happens in pair or something like that
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,list1))