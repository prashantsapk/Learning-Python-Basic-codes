# multiple level inheritance

class employee():
    name="Prashant"
    def printname(self):
        print(self.name)

class programmer(employee):
    role="Python programmer"
    def roleprint(self):
        print(self.role)

class typeofprogrammer(programmer):
    type="Backend developer"
    def printtypeofprogrammer(self):
        print(self.type)

a = typeofprogrammer()
print(a.type,a.name,a.role)

