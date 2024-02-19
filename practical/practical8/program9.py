num = 371
sum = 0
temp = num
while(temp>0):
    digit = temp%10
    sum += digit ** 3
    temp //= 10
if(num == sum):
    print(num, "is Armstrong's number")
else:
    print(num, "is not Armstrong's number")