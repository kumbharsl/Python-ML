#WAP to find the 7th odd number (start from 1)
x = int(input("Enter the number : "))
num = 0
count = 0
while num <= x:
    if num % 2 != 0:
        print(num, end=" ")
        count =+ 1
    num+=1
print(count)