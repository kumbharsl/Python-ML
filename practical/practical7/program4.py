#WAP to calculate the factorial of a given number.
num = int(input("Enter the Factorial num : "))
fact = 1
i = 1
while(i<=num):
    fact = fact*i
    i = i+1
print(f"Factorial of {num} is {fact}")