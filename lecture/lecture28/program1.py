# Inheristance method in python (28.12.2023)
class Parent():
    def __init__(self):
        print("In construction parent")
    
    def parentFunc(self):
        print("In parent function")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("In construction child")
    def childFunc(self):
        print("In child finction")

obj = Child()
obj.parentFunc()
obj.childFunc()