# multiple inheritance

class employee:
    name="prashant"
    def employeename(self):
        print(self.name)

class programmer:
    role="Python programmer"
    def employeerole(self):
        print(self.role)

class combined(employee,programmer): #multiple inheritance
    salary=10000
    def employeesalary(self):
        print(self.salary)

a= combined()
print(a.salary,a.role,a.name)