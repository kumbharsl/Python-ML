import matplotlib.pyplot as plt

# Employee data
emp_data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
            'Salary': [50000, 55000, 60000, 65000, 70000]}

# Calculate the total salary
total_salary = sum(emp_data['Salary'])

# Create a donut chart
plt.pie(emp_data['Salary'], labels=emp_data['Name'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Employee Salaries (Donut Chart)')
plt.show()

# Print the total salary
print('Total Salary: ${}'.format(total_salary))