my_list = [(1,2),(2,4),(3,4)]

myDict = dict(my_list) 

for k,v in myDict.items():
    v=v+1
    print(v)

print(myDict.values())


