import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # # find employees who have the highest salary in each of the departments
    # department_max_salary = employee.groupby('departmentId')['salary'].max().reset_index(name='max_salary')
    # employee = pd.merge(employee, department_max_salary, left_on='departmentId', right_on='departmentId', how='left')
    # employee_max_salary = employee[employee['salary'] == employee['max_salary']]
    # # obtain department names
    # department = department.rename(columns={'name': 'Department'})
    # employee_max_salary = pd.merge(employee_max_salary, department, left_on='departmentId', right_on='id', how='left')
    # employee_max_salary = employee_max_salary.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    # return employee_max_salary[['Department', 'Employee', 'Salary']]

    # let's try to write this more elegantly..
    # I should write my code with the output column names in mind, i.e. 'Department', 'Employee', 'Salary'
    
    # join and rename
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    df = df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})
    # compute max salary
    max_salaries = df.groupby('Department')['Salary'].max().reset_index(name='max_salary')
    df = pd.merge(df, max_salaries, on='Department', how='left')
    # return in the appropriate format
    return df[df['Salary'] == df['max_salary']][['Department', 'Employee', 'Salary']]