#WAP to print the count of all negative numbers from a given range
x=int(input("Start: "))
y=int(input("End: "))

count=0
for i in range(x,y):
    if i<0:
        count=count+i
        print(count)
