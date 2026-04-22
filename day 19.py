'''
polymorphism
--------------
---> this allows a object of different classes to be treated as instance of the same base class, with methods behaving differently based on the actual abject type.
print(len("python"))
print(len([1,2,3,4]))

Method overloading
---------------------
---> this defines multiple methods with th same name but different parameters like (number, type, or order) in the same class

'''
class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c

Cal = calculator()
print(Cal.add(2))
print(Cal.add(3,4))
print(Cal.add(5,7,8))

class calculator:
    def sub(self, a, b=0, c=0):
        return a-b-c

Cal = calculator()
print(Cal.sub(100))
print(Cal.sub(50,25))
print(Cal.sub(50,25,10))
'''
Method overriding
-------------------
---> this occurs in the child class, redefining a parent class method with the same signature for runtime

'''
class animal:
    def speak(self):
        return "Sound"

class dog(animal):
    def speak(self):
        return "woof"

Dog = dog()
print(Dog.speak())



class Music:
    def play(self):
        return "Playing general music"

class Rock(Music):
    def play(self):
        return "Playing Rock music "

class Classical(Music):
    def play(self):
        return "Playing Classical music "

class Pop(Music):
    def play(self):
        return "Playing Pop music "

m = Music()
r = Rock()
c = Classical()
p = Pop()

print(m.play())
print(r.play())
print(c.play())
print(p.play())
'''
operator overloading
-------------------------
----> this is cusomizes operator like +,- for user-define classes by implementing special method ....
eg... __add__,__sub__
'''
class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return someone(self.a +other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so)

'''
data abstraction
------------------
----> this hides complex implementation details, exposing anly essential features via abstract class or interface.
'''
from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
Circle = circle(5)
print(Circle.area())











        
