'''
Encapsulation
------------------
---> The principle of the building data(Attributes) and methods that operate on that data into a single unit, which is a class

'''
class BankAC:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposite(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance())

'''
Inheritance
--------------------
---> this allows a child class(subclass) to acquire the attributes and methods of the parent class(Base class) this is called Inheritance.
1.single Inheritance
------------------------
----> using single method of the class form base class is know as single.
example:
class parent:
    def display(self):
        print("This is parent method")

class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj = child()
obj.display()

2.Multiple Inheritance
------------------------
---->a child class inherits from more than one parent class ...

super()
-----------
---> this is used to call methods of the parent class from the child class.
'''
class parent:
    def display(self):
        print("This is parent method")

class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj = child()
obj.display()


class Father:
    def skill_1(self):
        print("Father: hard working")

class Mother:
    def skill_2(self):
        print("Mother: cooking ")

class Child(Father, Mother):
    def All_skills(self):
        print("child: coding")

Any = Child()
Any.skill_1()
Any.skill_2()
Any.All_skills()













