# WAP to calculate the sum of the first 10 even numbers.
sum=0
i=0
while i<=20:
    if i%2==0:
        sum = sum+i
    i=i+1
print(f"Sum of first 10 even numbers is : {sum}")