import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # bonus of an employee is 100% of their salary if:
    #   1. employee_id is odd
    #   2. name does not start with 'M'
    give_bonus = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary']
    employees['bonus'][~give_bonus] = 0
    return employees[['employee_id', 'bonus']].sort_values('employee_id')