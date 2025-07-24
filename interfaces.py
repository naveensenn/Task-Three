import zope.interface 

class Interface(zope.interface.Interface):
    x = zope.interface.Attribute("I am a zope.interface attribute")
    def method1(self, x):
        pass
    def method2(self):
        pass
  
@zope.interface.implementer(Interface)
class Class_name:
    def method1(self, x):
        return x**2
    def method2(self):
        return "I am a zope.interface attribute"


obj = Class_name()

print(obj.method1(4))