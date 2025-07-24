class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self._salary=salary
    
    @property
    def salary(self):
        print("Salary is")
        return self._salary
    
    @salary.setter  
    def setSalary(self,value):
        if value <= 0:
            print("Please Enter Valid Salary")
        
        self._salary=value
        
    @salary.deleter
    def delete_salary(self):
        print("Salary Deleted:")
        del self._salary
        
    @property
    def info(self):
        return f"name {self.name} salary {self.salary} age {self.age}"
        
e = Employee("Rahul",32,40000)

e.name

# del e._salary


print(e.info)
        
            