import matplotlib.pyplot as plt

# Employee data
emp_data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
            'Salary': [50000, 55000, 60000, 65000, 70000],
            'Experience': [5, 6, 7, 8, 9]}

# Create a scatter plot
plt.scatter(emp_data['Experience'], emp_data['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Employee Salaries vs. Years of Experience')
plt.grid(True)

# Show the plot
plt.show()