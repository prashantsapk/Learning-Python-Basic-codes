#instance attribute takes preference over the class attributes

class employee: # created a class
    name= "Prashant" # created attributes
    salary="100"
    role="Data security analyst"

prashant=employee()# now an object is created
print(prashant.name,prashant.salary,prashant.role) # class attribute 

prashant.language ="Nepali" # inheritance attributed/ newly created attribute
print(prashant.language) 

# you might say it is class atribute just value is different assigned
# instance attribute are that  attribute thats created by user differ than the class
# on this case its new so its instance attribute 

prashant.name="Rohan" # changed name here to rohan, or assigned new value 
# so if we try to print prashant.name, instance attribute will be given preference

print(prashant.name) # prints rohan