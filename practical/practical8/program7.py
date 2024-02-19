
num = 43521
n = 0
while(num>0):
    rem = num%10
    n = n*10+rem
    num = num//10
print(n)