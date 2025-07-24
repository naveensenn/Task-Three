
# from abc import ABC,abstractmethod

# @abstractmethod
# class Animal(ABC):
#     # def move(self):
#         pass

# class human(Animal):
#     def move(self):
#         print("I can walk with two legs")
        
# class bird(Animal):
#     def move(self):
#         print("I can fly")
        
# class Dog(Animal):
#     def move(self):
#         print("I can bark")
        

# H = human()
# b = bird()

# H.move()
# b.move()



class A:
    def mov(self):
        print("A")
        
class B:
    def __init__(self):
        pass
    
    def mov(self):
        print("B")
        
class C(A,B):
    
    def move(self):
        print("c")
        
obj = C()

obj.mov()
