# self parameter in easy way

class employee:

    def printfunction(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} age is {self.age}")

prashant=employee()
prashant.printfunction("PRASHANT",10)
