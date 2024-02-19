num = int(input("Enter the num : "))
sum = 0
n  = 1

while n<num:
    if num%n==0:
        sum=sum+n
    n+=1
if(sum==num):
    print(num, "is perfect number")
else:
    print(num, "is not perfect number")