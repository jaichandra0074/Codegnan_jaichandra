'''operators ---> an operator is a symbol that performs an operation on one or more values
                and produce a result.

operators are primarily used:
-->calculate values
-->compare values/inputs
-->make decisions
-->control the program flow

there are major seven categories of operators in python
-->arithmetic operators
-->assignment operators
-->comparision operators
-->membership operators(in,notin)
-->identity operators(is,is not)
-->bitwise operators
-->logical operators(and,or,not)
'''


#Arithmetic operators--> performs mathematical operations
#+-->addition ,- -->subtraction , * --> multiplication , / --> division ,
#** -->exponent, % --> modulus ,// --> integer division/floor division.

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)#returns in float value(quotient).
print(a**b)#return power(a,b)like (5,3)-->5*5*5=125.
print(a//b)#return only int values(quotient).
print(a%b)#returns remainder.

num1 = int(input("enter the first value  :"))
num2 = int(input("enter the second value :"))
result= (num1+num2)*4
print("the result is ",result)#standard notation

#f-string notation:
print(f'the result is {result}')
print(f' The result of {num1} and {num2} is {result}')



#Assignment operators
# =  assigning , += addition assignment , -= , *= , /= , //= , %= , **=
# they are majorly used for code repitations in application usage.

a = 4
b = 3
a += 2#--> a = a+2
print(a)
b += a
print(b)

#**=
a = 5
b = 3
print( f' the value of {a}**{b} is {a**b}')
a **= b
print( f' the value of a after using  **= is {a}')


#relational or comparision operators --> they always return the boolean values
# == is equal to , != not equals to, < lessthan , > greater than , >= ,<=
a = int(input("Enter a value:"))
b = int(input("Enter another value:"))
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)


#Membership operators(in  , not in)--> check for the existence of an object
#in collections. 

a = "codegnan"
print(type(a))
print('a' in a)# 1st a is character and 2nd a is a string_name
print('z' in 'sandeep')
print('z' not in 'sandy')

#another example
b = [12,6,3,4]
c = int(input("enter a number"))
print(c)
c in b 
print(f'The number {c} in {b} is { c in b } ')
print( c not in b)


#logical operators --> they are used to combine multiple conditins
#and ,or , not

age = 15
vote_right = True
print(age>=18 and vote_right)#if both conditions are true
                             #then only and should return true.

print(age >= 18 or vote_right)#returns true if any of the condition is true.

print(age >= 18  and  not vote_right)

print(age >= 18  or  not vote_right)



#Identity  operators--> they check the memory location and validate we use
#id()function it is different from == operator --> is , is not

a = [1,3,4]
b = [1,3,4]
print(a == b)
print(id(a)) #returns identity of a
print(id(b))    
print(a is b)   #false because both not in same memory location
print(a is not b)

c = b  #assigning b to c 
print(id(c))  #then b and c have same memory location 
print(c is b) #returns true because b,c have same memory location



#bitwise operators -->
print(5 & 3)#   5 --> 0101
            #   3 --> 0011
            #   do and (&) between  5,3 .
            #ans: 0001 answer is one 
                
print(5 | 3)#same like above do or operation for 5,3
            #we get answer 7.

#we have bin function
print(bin(5))#returns binary value of 5.

#Task ---> Now you have all operators create a checker Task.
#git add .
#git commit -m "operators usage"
#git push -u origin main
