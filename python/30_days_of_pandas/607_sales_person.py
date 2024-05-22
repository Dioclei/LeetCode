import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # obtain company id for company "RED"
    id_RED = company[company['name'] == "RED"]['com_id']
    # obtain all orders that are associated with that company
    orders_RED = orders[orders['com_id'].isin(id_RED)]
    # obtain all salesperson ids of those orders
    salesperson_ids_RED = orders_RED[['sales_id']]
    # concat and drop duplicates
    salesperson_ids_not_RED = pd.concat([salesperson_ids_RED, sales_person]).drop_duplicates(subset=['sales_id'], keep=False)
    return salesperson_ids_not_RED[['name']]
