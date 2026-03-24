''' string ---> string is a collection of char, which is represent by "" or '' and we can access the using indexing and also slicing
len() ---> len() method is used to get char present in the string or find the length of the string'''
name = "Neduri jaichandra dasaradha ramayya"
print(name)
print(name[7])
'''Traceback (most recent call last):
  File "C:/Users/hp/OneDrive/Desktop/codegnan_py/day_7.py", line 5, in <module>
    print(name[7,4,8])
TypeError: string indices must be integers, not 'tuple'
print(name[7,4,8])'''
print(name[7:13])
print(name[7:18])
so = name.replace("jaichandra","chandu")
print(name)
print(so)
print(name[-12:-1])
#print(name[100])

details = "hello everyone i'm neduri jaichandra dasaradha ramayya, i am learning python fullstack and ai tools at codegnan"
print(f"my name is {details[19:55]}")
print(f"enrolled at course of {details[-42:-11]}")
print(f"institue of {details[-8:]}")
#reverse
spy_movie ="dhurandhar"
print(spy_movie[::-1])
#length
print(len(spy_movie))
print(len(details))
#note :- we can convert a string into integer, if the contain only integer value ......
'''so = "123p"
num = int(so)
print(type(num))'''


'''methods of the string 
--------------------------------------
split()---> remove space, and the output is in the list[] it will give the sparated things in each index

syntax------>variable_name.split("substring")

lower() ----> this is used to convert all letter into lower cases

syntax -------> variable_name.lower("sunstring")

upper() ----> this is used to convert all letter into upper cases

syntax -------> variable_name.upper("sunstring")

replace() -------> this is used to replace the old string with new string

syntax -----> variable_name.replace("old string","new string")
'''
print(name.split())
print(name.split("dasaradha"))
print(name.lower())
print(name.upper())
some = "python is a programming language"
if "A" in some:
    print("yes, it is there")
else:
    print("no,it is not there")
print(some)
print(some.replace("programming","normal"))
game = "python is a programming language"
if "is" in game:
    print("yes, it is there")
else:
    print("no,it is not there")

letter = input("enter the letter: ").lower()

if letter in "aeiou":
    print("it is a vowel")
else:
    print("it is a consonant")
































