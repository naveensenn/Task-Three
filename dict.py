# d = {1:"a",2:"b",3:"c",4:{5:"d",6:"e",7:"f"}}

# keys=[]

# for k,v in d.items():
#     keys.append(k)
    
#     if isinstance(v,dict):
#         keys.extend(v)
        
# print(keys)



d1 = {1:"a",2:"b",3:"b"}
d2 = {4:"d",5:"e",6:"f"}

# level = ["Level 1","level 2"]

dict_lst = [d1,d2]

res = dict()

res["1"]=d1
res["2"]=d2
res["3"]=[d1,d2]

print(res)