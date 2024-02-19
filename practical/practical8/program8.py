num = 2332
n = 0
while(num>0):
    rem = num%10
    n = n*10+rem
    num = num//10
if(n == 2332):
    print(n, "is palindrome number")
else:
    print(n, "is not palindrome number")