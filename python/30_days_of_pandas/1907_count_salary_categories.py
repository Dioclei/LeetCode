import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['Low Salary'] = accounts['income'] < 20000
    accounts['Average Salary'] = (accounts['income'] >= 20000) & (accounts['income'] <= 50000)
    accounts['High Salary'] = accounts['income'] > 50000
    df = accounts[['Low Salary', 'Average Salary', 'High Salary']].agg(sum)
    df = pd.DataFrame({
        'category': df.index,
        'accounts_count': df.values
    })
    return df