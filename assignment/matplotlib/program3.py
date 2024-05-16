import matplotlib.pyplot as plt

# Employee data
emp_data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
            'Salary': [50000, 55000, 60000, 65000, 70000],
            'Year': [2015, 2016, 2017, 2018, 2019]}
emp_data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
            'Salary': [70000, 75000, 80000, 85000, 90000],
            'Year': [2015, 2016, 2017, 2018, 2019]}

# Create a line graph
plt.plot(emp_data['Year'], emp_data['Salary'])
plt.plot(emp_data1['Year'], emp_data1['Salary'])
plt.xlabel('Year')
plt.ylabel('Salary')
plt.title('Employee Salaries Over Time')
plt.legend()

# Show the plot
plt.show()