import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates().sort_values(ascending=False)
    val = df.iloc[1] if df.shape[0] >= 2 else None
    return pd.DataFrame({'SecondHighestSalary': [val]})