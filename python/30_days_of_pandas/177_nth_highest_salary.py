import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    # salaries is a Series object
    if N > 0 and salaries.shape[0] >= N:
        val = salaries.iloc[N-1]
    else:
        val = None
    title = 'getNthHighestSalary(' + str(N) + ')'
    return pd.DataFrame(data={title: [val]})

def test():
    df = pd.DataFrame({'id': [1, 2], 'salary': [100, 200]})
    print(df)
    print(nth_highest_salary(df, 2))

test()