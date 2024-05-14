# 7. Create a DataFrame from the dictionary {'A': [1, 2, 3], 'B': [4, 5, 6]}. Print the
# information about the DataFrame using a pandas function.

# Create a pandas DataFrame from the dictionary {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print("Information about the DataFrame:")
print(df.info())