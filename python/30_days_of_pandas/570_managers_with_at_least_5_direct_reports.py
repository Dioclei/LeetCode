import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    reports_count = employee.groupby('managerId').size().reset_index(name='reports_count')
    employee = pd.merge(employee, reports_count, left_on='id', right_on='managerId', how='left')
    return employee[employee['reports_count'] >= 5][['name']]