# Create a DataFrame from the dictionary {'X': [11, 12, 13], 'Y': [14, 15, 16], 'Z': [17,
# 18, 19]}. Print the DataFrame and then print its columns.
import pandas as pd

# Create a dictionary {'X': [11, 12, 13], 'Y': [14, 15, 16], 'Z': [17, 18, 19]}
data = {'X': [11, 12, 13], 'Y': [14, 15, 16], 'Z': [17, 18, 19]}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Print the columns of the DataFrame
print("\nColumns of DataFrame:")
print(df.columns)