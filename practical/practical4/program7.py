#WAP to prints numbers which are divisible by 3 and 5 both in a given range.
x=int(input("Start: "))
y=int(input("End: "))

for i in range(x,y):
    if i>0:
        print(i,end =" ")