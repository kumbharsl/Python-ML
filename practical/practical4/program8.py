#WAP to prints numbers which are divisible by 3 and 5 both in a given range.
x=int(input("Start: "))
y=int(input("End: "))

for i in range(x,y):
    if i%3==0 and i%5==0:
        print(i)