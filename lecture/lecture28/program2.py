class Parent():
    def __init__(self):
        print("In construction parent")
    
    def parentFunc(self):
        print("In parent function")

class Child(Parent):
    pass
    #def __init__(self):
        #print("In construction child")

obj1 = Child()
obj1.parentFunc()