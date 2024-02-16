def fun(x,y):
    while(x<y):
        yield x
        x = x + 1

for val in fun(1,11):
    print(val)

fun(1,11)