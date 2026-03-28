'''
we can store data as key : value
keys ---- are union and we can only give immutable data types in the keys
values --- we all data types (immutable and mutable)
{}

methods
------------
keys() --- this method is used to get all keys from the dict

values() --- this method is used to get all values from the dict

clear() --- this method is used to delete the dict


'''
amdox_chandu = {"name":"neduri jaichandra dasaradha ramayya",
              "pin_number":113374,
              "role":"intern",
              "salary":10000,
              "location":"banguluru",
              "wfh":"avalable",
              "education":"B.TECH"}
print(amdox_chandu.keys())
print(amdox_chandu.values())
#print(amdox_chandu.clear())
pin = int(input("enter the pin : "))
if pin is amdox_chandu['pin_number']:
    print(amdox_chandu)
else :
    print("you are not correct")
'''
set{} ---> set data type is a unordered collection and it never allow deplicates

methods
---------
union() ---> this is used add or get 2 different sets without duplicates

intersection ---> this method is used to find out common items for 2 sets

difference ---> this method is used to find the different once from the 2nd set
'''
any = {1,2,3,4,5}
so = {3,4,5,6,7,8,9,10,11}

print(any.union(so))
print(any.intersection(so))
print(any.difference(so))
print(any.remove(4))




