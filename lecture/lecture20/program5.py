# 8) find()
'''Searches the  string for a specified value and return the position 
of where it  was found'''
str1 = input("Enter main string : ")
sub = input("Enter sub string : ")

if sub in str1:
    print(sub + " found")
else:
    print(sub + " not found")

n = str1.find(sub)
if n ==-1:
    print(sub+"Not found")
else:
    print(sub+" found at index ",format(n))