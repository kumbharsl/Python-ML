#WAP to print the sum of all numbers from a given range.
x = int(input("Start = "))
y = int(input("End = "))

sum=0
for i in range(x,y):
    sum+=i
    print(sum,end = " ")