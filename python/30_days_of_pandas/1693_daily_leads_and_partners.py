import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    distinct_leads = daily_sales.groupby(['date_id', 'make_name'])['lead_id'].nunique().reset_index(name='unique_leads')
    distinct_parts = daily_sales.groupby(['date_id', 'make_name'])['partner_id'].nunique().reset_index(name='unique_partners')
    return pd.merge(distinct_leads, distinct_parts, on=['date_id', 'make_name']).fillna(0)