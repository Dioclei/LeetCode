import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    df = employees.groupby(['event_day', 'emp_id']).sum()
    df = df[['total_time']]
    df = df.reset_index()
    df = df.rename(columns={'event_day': 'day'})
    return df