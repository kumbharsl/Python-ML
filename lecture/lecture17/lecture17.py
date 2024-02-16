#methods from list class

'''
1.delete
2.count
3.index
4.reverse
5.sort
6.copy
'''

player = ["Rohit","Shubman","Virat","Shreyas","KLRahul"]

print(player)
player.append("SKY")
print(player)
player.extend(["jaddu","Bumrah","jaddu"])
print(player)
player.insert(3,"hardik")
print(player)
player.remove("SKY")
print(player)
print(player.count("jaddu"))
print(player.index("jaddu"))
player.reverse()
print(player)
player.sort()
print(player)