import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').size().reset_index(name='orders').sort_values('orders', ascending=False)
    return orders[['customer_number']][:1] # slicing deals with empty tables too