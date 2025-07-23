# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def show(self):
#         print(self.name)
#         print(self.salary)
        

# e1 = Employee("Sam",25000)
# setattr(e1,"age",25)
# print(getattr(e1,"age"))
# print(hasattr(e1,"address"))
# e1.show()


# class Parent:
#     def __init__(myself):
#         myself.setattr = "Parent Class"
        
#     def show(myself):
#         print(myself.setattr)     
        

# class Child(Parent):   
#     def __init__(myself):
#         super().__init__()
#         myself.child_arr = "Child Class"
        
#     def display(myself):
#         myself.show()
#         print(myself.child_arr)
        
# c1 = Child()

# c1.display()


# class Abc:
#     def __init__(self):
#         print("Constructor Called")
        
#     def __del__(self):
#         print("Destructor Called")
        
# a1 = Abc()




# class Employee:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance
        
#     def display(self):
#         print(self.name)
#         print(self.__balance)
        
# obj = Employee("Rahul",50000)
# obj.display()



# class Dog:
#     def sound(self):
#         return "bark"

# class Cat:
#     def sound(self):
#         return "Meow"
    
# class Lion:
#     def sound(self):
#         return "Roar"
    
# animals = [Cat(),Dog(),Lion()]

# for animal in animals:
#     print(animal.sound())
        
        
        

# class Animal:
#     def sound(self):
#         return "Woof !"
    
# class Domestic(Animal):
#     def home(self):
#         return "Lives with human"
    
# class Dog(Domestic):
#     pass
    
    
# dog = Dog()

# print(dog.sound())


from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    
    def engine_start(self):
        pass
    
    @abstractmethod
    def engine_stop(self):
        pass
    
class Car(Vehicle):
    def engine_start(self):
        return "Engine Started"
    
    def engine_stop(self):
        return "Engine Stopped"
    
v=Car()

print(v.engine_start())

