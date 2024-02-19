num = 942111423

count = 0
while (num>0):
    num = num//10
    if(num%2==1):
        count +=1
print(count)