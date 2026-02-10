# lets learn about the class method in python

class employee:
    name="Prashant"
    @classmethod  # 
    def printname(cls):
        print(f"The name is {cls.name}") 

a = employee()
a.name="Laxmi" #inheritance is always provided preference
#but when i use the class method for this printname function
#it uses class varialbe name="Prashant" instead of that inheritance
# thats why we use class method
a.printname()