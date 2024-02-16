def decorFun(func):
    print("In decor fun")

    def wrapper(*args):
        print("Start wrapper")
        val = func(*args)
        print("End wrapper")
        return val
    return wrapper

@decorFun
def normalFun(x,y):
    print("In normal fun")
    return x+y
ret = normalFun(10,20)
print(ret)