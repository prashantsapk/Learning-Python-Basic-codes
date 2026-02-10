class employee:
    @property # property is nothing, function that behaves like variable
    def printname(self): 
        self.name="Prashant"
        return self.name

    @printname.setter
    def age(self, value):
        if (value == "Prashant"):
            print("Welcome prashant")
        else:
          print("You aren't prashant")

a = employee()
print(a.printname)
# a.printname="Prashant" thats where setter comes place

a.age ="Rohan" # its same like running a.age("Here you enter the value")