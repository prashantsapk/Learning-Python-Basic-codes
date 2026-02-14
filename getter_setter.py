# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property


class Employee():

    def __init__(self,_salary,_increment):
        self._salary=_salary
        self._increment=_increment

    @property
    def salary(self):
        return self._salary

    @property
    def increment(self):
        return self._increment

    @property
    def salaryafterincrement(self):
        return self._salary*self._increment # property makes function a variable like obj.salaryafterincrement instead of obj.salaryafterincrement()

    @salaryafterincrement.setter
    def salaryafterincrement(self,newvalue): # we use this setter shit for validation, it doesn't return value, so like here we are updating or setting value of that increment as newvalue
        self._increment=newvalue
        
obj = Employee(100,0.1)
obj.salaryafterincrement = 10
print(obj.salaryafterincrement)