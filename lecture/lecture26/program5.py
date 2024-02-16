def decorFun(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    return wrapper

@decorFun
def normalFun():
    print("In inner fun")

normalFun()