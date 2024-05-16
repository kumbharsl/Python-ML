import matplotlib.pyplot as plt

# Employee data
emp_data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
            'Salary': [50000, 55000, 60000, 65000, 70000]}

# Create a bar chart
plt.bar(range(len(emp_data['Name'])), emp_data['Salary'])
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.title('Employee Salaries')
plt.xticks(range(len(emp_data['Name'])), emp_data['Name'])

# Show the plot
plt.show()