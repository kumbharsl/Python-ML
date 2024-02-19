#WAP to print all Even numbers from a given range
x=int(input("Start = "))
y=int(input("End = "))

for i in range(x,y):
    if i%2==0:
        print(i, end =" ")