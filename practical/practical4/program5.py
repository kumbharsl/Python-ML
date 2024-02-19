#WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100
x=int(input("Enter start of range - "))
y=int(input("Enter end of range - "))

for i in range(x,y):
    if i%7==0 and i%3!=0:
        print(i)