# 4. Using the list [1, 2, 3, "DataFrame", True, [70, 80, 90]], slice it to get the last three
# elements in reverse order. Print the sliced list.

my_list = [1, 2, 3, "DataFrame", True, [70, 80, 90]]

# Slice the list to get the last three elements in reverse order
sliced_list = my_list[-3:][::-1]

# Print the sliced list
print(sliced_list)