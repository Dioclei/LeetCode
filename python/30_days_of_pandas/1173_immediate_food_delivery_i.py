import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['is_immediate'] = delivery['order_date'] == delivery['customer_pref_delivery_date']
    percentage = delivery['is_immediate'].sum() / delivery['is_immediate'].shape[0] * 100
    percentage = round(percentage, 2)
    return pd.DataFrame({'immediate_percentage': [percentage]})