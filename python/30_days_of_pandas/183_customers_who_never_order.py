import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_who_didnt_order = pd.concat((customers[['id']], orders[['customerId']].rename(columns={'customerId': 'id'}))).drop_duplicates(keep=False)
    print(customers_who_didnt_order)
    customer_names = customers[customers['id'].isin(customers_who_didnt_order['id'])][['name']]
    customer_names.rename(columns={'name': 'Customers'})
    return customer_names
