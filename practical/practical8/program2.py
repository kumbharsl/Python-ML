num = int(input("Enter the num : "))
i = 1
count = 0
while (num>i):
    if(i%num==0):
        count+=1
    i+=1
if(count==1):
    print(num,"is prime number")
else:
    print(num,"is prime number")