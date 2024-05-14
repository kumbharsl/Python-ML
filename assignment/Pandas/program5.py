# 5. Convert the list [5, 10, 15, 20, 25] to a pandas Series and print the Series. Then,
# access and print the third element of the Series.

# Convert the list [5, 10, 15, 20, 25] to a pandas Series
s = pd.Series([5, 10, 15, 20, 25])

# Print the Series
print("Series:")
print(s)

# Access and print the third element of the Series
print("\nThird element of the Series:")
print(s[2])