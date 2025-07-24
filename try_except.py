# try :
#     f = open("hello.py","w")
#     try:
#         f.write("I am New Developer")
#     except :
#         print("Something went wrong")
#     finally:
#         f.close()
#         print("File closed successfully")
# except:
#     print("Sorry for inconvience")
# # finally:
# #     print("Printed Successfully")



# try:
#     value = int(input("Enter Number: "))
#     try:
#         result = int(input("Enter Second Number: "))
        
#         try:
#             result=result/value
#         except ZeroDivisionError:
#             print("Cannot Divide by Zero")
#     except ValueError:
#         print("Enter Valid Number")
# except:
#     print("Something Went Wrong")
# finally:
#     print("Executed Successfully")



# Custom Exception 1
# class MyException(Exception):
#     def __init__(self,message):
#         self.message = message
#         super.__init__(message)
        
    
# def divide(a,b):
#     if b==0:
#         raise MyException("You Can't divide by Zeo",400)
#     return a/b
    
# try:
#     result = divide(10,0)
#     print(result)
# except MyException as e:
#     print(f"caught an error {e}")
    
    

# # Custom Exception Two
# class MyCustomException(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#         super().__init__(msg)

        
# def Value(a,b):
#     if a<b:
#         raise MyCustomException("A must be greater than B",500)
    

# try:
#     result = Value(8,9)
#     print("A is greater than B ")
    
# except MyCustomException as e:
#     print(f"Something Went Wrong: {e}")




with open("hello.py","r") as file:

    data=file.read()
print(data)
    