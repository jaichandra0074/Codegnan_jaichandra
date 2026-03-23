# condition statements are decision making statements
'''
if statement ---> this if statement is used to check any condition, if the condition becomes true then it will enter in side the(if statement)
example: age =int(input("Enter your age : "))
if age >= 18:
    print("your age is 18 or above")
if-else statement
if-elif-else statement
code Q
'''

#1 if-else statement --------------
student_att = int(input("enter your attendance : "))
if student_att >= 75:
    print("you can directly sit in the sem exam")
else :
    print("you cannot enter in the exam hall")
#2
age = int(input("Enter your age:"))
if age >=18:
    print("you can vote now")
else :
    print(f"you cannot vote and you have wait {18-age} years")
#3
total_amt = int(input("Enter you total shopping money: "))
if total_amt >=200:
    print("no delivery cost")
else:
    print(f"add {200 - total_amt} to your cart")

#4 if-elif-else statement-------------
n = int(input("Enter how many hours: "))

if n <= 2:
    print("The price of the parking lot is:", n * 100)

elif 3 <= n <= 5:
    k = 200 + (n - 2) * 50
    print("The price of the parking lot is:", k)

elif n > 5:
    a = 350 + (n - 5) * 20
    print("The price of the parking lot is:", a)

else:
    print("Error")
#5
marks = int(input("Enter the marks of the student : "))

if marks > 90:
    print("you got O grade for", marks)

elif marks >= 85:
    print("you got A+ grade for", marks)

elif marks >= 80:
    print("you got A grade for", marks)

elif marks >= 75:
    print("you got B+ grade for", marks)

elif marks >= 70:
    print("you got B grade for", marks)

elif marks >= 65:
    print("you got C+ grade for", marks)

elif marks >= 60:
    print("you got C grade for", marks)

elif marks >= 55:
    print("you got D+ grade for", marks)

elif marks >= 50:
    print("you got D grade for", marks)

elif marks >= 45:
    print("you got Pass grade for", marks)

else:
    print("you got Fail grade for", marks)


#6 calculator
num1 = float(input("enter 1st number : "))
num2 = float(input("enter 2nd number : "))
operator = input("enter your operator : ")

if operator == "+":
    print("the sum of two number is", num1 + num2)

elif operator == "-":
    print("the sub of two number is", num1 - num2)

elif operator == "*":
    print("the multiple of two number is", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("the division of two number is", num1 / num2)
    else:
        print("cannot divide by zero")

else:
    print("error")
#7
num_1 = float(input("Enter 1st number : "))
num_2 = float(input("Enter 2nd number : "))
user_choice = int(input("enter your choice : \n1.ADD \n2.SUB \n3.MUL \n4.DIV \n"))
if user_choice == 1:
    print("the sum of two number is", num_1 + num_2)

elif user_choice == 2:
    print("the sub of two number is", num_1 - num_2)

elif user_choice == 3:
    print("the multiple of two number is", num_1 * num_2)

elif user_choice == 4:
    if num2 != 0:
        print("the division of two number is", num_1 / num_2)
    else:
        print("cannot divide by zero")

#8 : even or odd
number = int(input("enter your number : "))
if number % 2 == 0 :
    print(f"{number} is even number ")
else :
    print(f"{number} is odd number ")

# 9 : positive or negetive
number = int(input("enter the number : "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("The number is zero")
    








