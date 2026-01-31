class employee:
    name= "ram" # this is just attribute nothing else
    age = "10"
    salary = "10000"


# now how can you make objects?

ram = employee() # this is how the object is created
# now we need to do something more, class attribute and instance attribute

print(ram.name, ram.age) # what is this ? class attribute 
ram.role= "Data security analyst" # what is this ? instance attribute 
print(ram.role)

