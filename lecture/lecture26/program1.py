# args 0 or any number of parameter.
def normalFun(*args):
    sumData = 0
    for i in args:
        sumData = sumData + i
    return sumData
print(normalFun(10,20,30))