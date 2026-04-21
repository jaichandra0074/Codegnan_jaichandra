'''
multi-level
-------------
---> This occurs when a class inherits from a child class, creating a grandparent --> parent --> child in this structure

'''
class Grandparent:
    def Show_Grandparent(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")

class Child(Parent):
    def Show_Child(self):
        print("I'm Child")

any = Child()
any.Show_Grandparent()
any.Show_Parent()
any.Show_Child()



class Mobile:
    def basic_features(self):
        print("Basic Mobile Features: Calling, SMS")

class Android(Mobile):
    def android_features(self):
        print("Android Features: Apps, Play Store, Customization")

class Update(Android):
    def last_update(self):
        print("System Update: Security Patch, New UI, Bug Fixes")

class Update2(Android):
    def latest_update2(self):
        print("System Update: Refreshing rate, New UI, change of logos")

phone1 = Update()
phone1.basic_features()
phone1.android_features()
phone1.last_update()

print("-----")

phone2 = Update2()
phone2.basic_features()
phone2.android_features()
phone2.latest_update2()
'''
Hierchical
---------------
----> This occurs when multiple child classes inherit from a single parent class, this process is called hierchical

'''

class parent:
    def Parent_(self):
        print("i am parent")

class child_1(parent):
    def child_(self):
        print("i am 1st child")
        
class child_2(parent):
    def _child(self):
        print("i am 2nd child")

class child_3(child_1, child_2):
    def child(self):
        print("i am the child")

thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()
'''
hybrid inheritance
-------------------
--->this is a cimbination of two or more th=ype of inheritance, such as single multiple, bulti-level, or hierachical all this in a single class ...


'''
class grandparent:
    def grandparent(self):
        print("I'm Grandparent")
        
class parent:
    def Parent_(self):
        print("i am parent")

class child_1(parent):
    def child_(self):
        print("i am 1st child")
        
class child_2(parent):
    def _child(self):
        print("i am 2nd child")

class child_3(child_1, child_2, grandparent):
    def child(self):
        print("i am inherite from Grandparent class and child_1, child_2")

thing = child_3()
thing.grandparent()
thing.Parent_()
thing.child_()
thing._child()
thing.child()











        
