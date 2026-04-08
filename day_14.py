'''
functions() ---> this is a block of code which is reuseable.
            ---> two types 1.build-in or In-build
                           2.user define

1)build-in or In-build:
---> they comes in the program itself and those are already define....
eg...
------> print(),sum(),map().........

2)user define
-----> this is created by person who is developing or using for development

note:
------
--->it's starts with def keyword followed by func name
---> and it has calling func...
def func_name():
    --------------
    ---------------
    --------------
    ---------------
func_name()
def func_name(a,b) are called parameters
func_name(a,b) are called arguments

'''
#write a code for even numbers or odd numbers

a= int(input("enter the number : "))
def func_even_odd(a):
      if a%2 == 0 :
            print(f"{a} is even number")
      else :
            print(f"{a} is odd number")
func_even_odd(a)


a= int(input("enter the number : "))
def func_even_odd(a):
      if a%2 == 0 :
            print(f"{a} is even number")
      else :
            print(f"{a} is odd number")
func_even_odd(a-2) #argumentrs can be changeable and it consider argument value only

# do the prime number
a = int(input("enter the number : "))
count = 0
def func_prime(a,k):
      for j in range(1,a+1):
            if a % j ==0:
                  k+= 1
      if k == 2:
            print(f"{a} is a prime")
      else :
            print(f"{a} is not a prime")
func_prime(a,count)
#palidrom
text = input("enter the string: ")
rev = ""

def palindrome(text, r):
    for ch in text:
        r = ch + r
    
    if text == r:
        print("It is palindrome")
    else:
        print("It is not palindrome")

palindrome(text, rev)


a = [5,6]
b = [5,6]
print(a is b)
print(a == b)
