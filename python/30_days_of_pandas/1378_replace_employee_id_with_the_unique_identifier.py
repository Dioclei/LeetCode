import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, employee_uni, left_on=['id'], right_on=['id'], how='left')
    # important to use how='left' because we only want to use the ids present in the employees dataframe
    # i.e attach unique ids to the employees
    # using how='outer' will lead to irrelevant ids in employee_uni to also be included
    return df[['unique_id', 'name']]

employees = pd.DataFrame({'id': [1, 7, 11, 90, 3], 'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']})
employeeUNI = pd.DataFrame({'id': [3, 11, 90], 'unique_id': [1, 2, 3]})
print(replace_employee_id(employees, employeeUNI))