def decorFun(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End main")
    return wrapper
@decorFun
def normalFun():
    print("hello in Normal fun")

normalFun()