class Employee:
    def __init__(self):
        self.employee={}
    
    def add_employee(self,name,department,salary):
        self.employee[name]={"department":department,"salary":salary}
