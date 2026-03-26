print(19 + 20)
print("python "+"language")
print([1,2]+[3,4])
'''
concatenation
---------------------
this is nothing but, a(+) behavi.....
case-1
---------
integers --- this will act as addition for the int
---------
case-2
concatenation is not able to add the two different data types 
File "C:/Users/hp/OneDrive/Desktop/codegnan_py/day_9.py", line 15, in <module>
    print(3 + [1,2])
TypeError: unsupported operand type(s) for +: 'int' and 'list'
    print(2 + "knr")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(23.0 +"king")
TypeError: unsupported operand type(s) for +: 'float' and 'str'

tuple()-----> tuple is a collection of different datatypes and this is represented by (),separated by (,)
eg....
thing = (1,"ramayya",[12,4],(6,7))
'''

thing = (1,"ramayya",[12,4],(6,7))
print(thing)
print(thing[3][0])
king = (12,43,56,"python",(23,"ramayya",[99,"python is a programming language",("dasaradha ramayya",[67,34])]))
print(king)
print(king[4][2][1][6])
#swapping
num = 2
num_2 = 90
print(f"before swapping num = {num} and num_2 = {num_2}")
num, num2 = num_2, num
print(f"after swapping num = {num} and num_2 = {num_2}")

#leap year
leap_year = int(input("Enter the year : "))
if (leap_year % 4 == 0 and leap_year % 100 !=0) or leap_year % 400 == 0 :
    print(f"yes, {leap_year} is a leap year")
else :
    print(f"No, {leap_year} is not leap year")
