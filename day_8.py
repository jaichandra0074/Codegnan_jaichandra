'''24 hours to 12 hours'''

time_aday = input("enter the 24 hours time : ")
parts_ = time_aday.split(":")
print(parts_)
hours_ = int(parts_[0])
print(hours_)
min_ = int(parts_[1])
print(min_)
if hours_ >= 13 and min_ < 60:
    print(f"{time_aday} is converted into {hours_ - 12}:{min_} pm ")
else :
    print(f"you have enter the hours or min are incorrect")


list_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4][2][0][3])
list_2 = ["neduri","jaichanrda","dasaradha","ramayya",[27,23,90,["jnnurm","colony"],"vepagunta"]]
print(list_2[4][3][0])
''' ------------------ methods of list ---------------------
append() ----> this method is used to add new items into list it will only go for the last index of the list

syntax ----> variable_name.append(item)

extend()-------> this method is used to add items to list in the index,where each item or sunstring is each index in the list

syntax ----> variable_name.extend(item)

remove()-----> this method is used to remove item from the index 

syntax ----> variable_name.remove(item)

pop() --------> this method will delete the item or value based on the index position

syntax ----> variable_name.pop(index value)

mutable ---> i can directly modify on the particular variable
immutable ----> i can not modify directly on the variable
'''
list_3 = [1,2,3,4,5]
print(list_3)
list_3.append(6)
print(list_3)
list_3.append([3,4])
print(list_3)
list_3.extend([23.0,75.0,65])
print(list_3)

list_4 = [1,2,3,4,5,6,7]
list_4.remove(2)
print(list_4)
list_2.remove("ramayya")
print(list_2)
list_4.pop(1)
print(list_4)
