#WAP to print all the character value of the given ASCII value range from the user
x = int(input("Enter the start of range :"))
y = int(input("Enter the end of range :"))

for i in range(x,y):
    print("ACSII value : "  + str(i) + ", Character:",chr(i))