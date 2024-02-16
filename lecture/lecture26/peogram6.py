def decorFun(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    return wrapper
