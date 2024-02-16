def decorRun(func):
    def wrapper(*args):
        print("Start wrapper1")
        func()
        print("End wrapper1")
    return wrapper

def decorFun(func):
    def wrapper(*args):
        print("Start wrapper2")
        func()
        print("End wrapper2")
    return wrapper

def decorGun(func):
    def wrapper(*args):
        print("Start wrapper3")
        func()
        print("End wrapper3")
    return wrapper

@decorGun
@decorFun
@decorRun
def normalFun():
    print("In normal fun")
normalFun()