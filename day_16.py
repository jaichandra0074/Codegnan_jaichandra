'''
lambda function()
-------------------------
-------> this is also called anonymous function....
-------> a lambda function can take n number of arguments but have only on expression

syntax
-------
       lambda(keyword) arguments : expression 
'''
any = lambda so : so + 10
print(any(6))

some = lambda an, how, do : (how - an)*do
print(some(4,9,2))

king = lambda sing,dance : dance - sing
print(king(7,3))

ch = lambda an,du : an*du
print(ch(9,27))

ra = lambda ma,yya : ma/yya
print(ra(100,25))
'''
List comprehension:
--------------------
----> this is offers the shorter syntax when you want to create a new list from the existing list

syntax
------
         variable_name = [expression loop and condition]
'''
old_list = [2,4,5,6,7,1]
new_list = [j for j in old_list if j%2 == 0]
print(new_list)
