# single level inheritance

class employee:
    department="Staff"
    
    def staff(self):
        print(self.department)

class programmer(employee): #single inheritance
    programmer="Python"
    def pythonprogrammer(self):
        print(self.programmer)

a = programmer()
print(a.programmer,a.department)