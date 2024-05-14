import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    df = df['customer_id'].drop_duplicates()
    return pd.DataFrame({'rich_count': [df.count()]})
    # can also use nunique to count
    # count = df['customer_id'].nunique()
    # return pd.DataFrame({'rich_count': [count]})