# 6. Create a DataFrame from the dictionary {'A': [10, 20], 'B': [30, 40]}. Access and
# print the 'A' column.

# Create a pandas DataFrame from the dictionary {'A': [10, 20], 'B': [30, 40]}
df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})

# Access and print the 'A' column
print("'A' column:")
print(df['A'])