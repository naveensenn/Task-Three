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




# with open("hello.py","a") as file:

#     data=file.write("\nHii I am New Developer")
# print(data)



# with open("new.py","w") as file:
#     data=file.write("Hii Welcome to python")
# print("File created successfully!")


# import csv

# with open("test.csv",mode="r") as file:
#     data=csv.reader(file)
    
#     for line in data:
#         print(line)


# f = ['Name', 'Branch', 'Year', 'CGPA']
# r = [
#     ['Nikhil', 'COE', '2', '9.0'],
#     ['Sanchit', 'COE', '2', '9.1'],
#     ['Aditya', 'IT', '2', '9.3'],
#     ['Sagar', 'SE', '1', '9.5'],
#     ['Prateek', 'MCE', '3', '7.8'],
#     ['Sahil', 'EP', '2', '9.1']
# ]

# with open("test.csv",'a',newline='') as file:
#     csvfile = csv.writer(file)
    
    
#     csvfile.writerow(f)
#     csvfile.writerows(r)
    
# print("file created successfully!")




# d = [
#     {'name': 'Nikhil', 'branch': 'COE', 'year': '2', 'cgpa': '9.0'},
#     {'name': 'Sanchit', 'branch': 'COE', 'year': '2', 'cgpa': '9.1'},
#     {'name': 'Aditya', 'branch': 'IT', 'year': '2', 'cgpa': '9.3'},
#     {'name': 'Sagar', 'branch': 'SE', 'year': '1', 'cgpa': '9.5'},
#     {'name': 'Prateek', 'branch': 'MCE', 'year': '3', 'cgpa': '7.8'},
#     {'name': 'Sahil', 'branch': 'EP', 'year': '2', 'cgpa': '9.1'}
# ]

# f = ['Name', 'Branch', 'Year', 'CGPA']


# with open("new.py","a",newline="") as file:
#     csvWriter=csv.DictWriter(file,fieldnames=f)
    
#     csvWriter.writeheader()
    
#     csvWriter.writerows(d)
    
# print("File Created Successfully!")
    
    
import json

# data = {
#     "name": "Alice",
#     "age": 30,
#     "occupation": "Engineer"
# }

# file=open("data.json","w")   
# json.dump(data,file,indent=4)

# print("File Created Successfully!")
# file.close()


# file = open("data.json","r")
# data=json.load(file)

# print(data['name'])
# print(data)

