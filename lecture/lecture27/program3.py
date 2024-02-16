def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30
    print("End fun")
    yield

ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))