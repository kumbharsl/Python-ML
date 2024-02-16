# **args it's means keyword are argument.
def normalFun(**args):
    sumData = 0
    for k,v in args.items():
        sumData = sumData + v
    return sumData
print(normalFun(x=10,y=20,z=30))