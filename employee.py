class Employee:
    def __init__(self,name,department,salary):
        self.employe={}
        self.name=name
        self.department=department
        self.salary=salary
    
    @property
    def employee(self):
        return f"Name-{self.name} Department-{self.department} Salary-{self.salary}"
    
    @employee.setter
    def addEmployee(self,name,department,salary):
        self.employe[name]={"Department":department,"Salary":salary}
        print("Data Added successfully")
    
        
    @employee.deleter
    def removeSalary(self):
        del self.salary
    
    @employee.deleter
    def removeDepartment(self):
        del self.department
        
e1 = Employee("Rahul","Technical",50000)
e2 = Employee("Ram","Marketing",25000)
print(e1.employee)
print(e2.employee)
