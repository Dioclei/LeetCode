import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date').agg(lambda x: sorted(set(x))).reset_index()
    df['products'] = df['product'].str.join(',')
    df['num_sold'] = df['product'].str.len()
    return df[['sell_date', 'num_sold', 'products']]

    # editorial solution:
    # uses agg differently, to output 2 different columns 'products' and 'num_sold'
    # groups = activities.groupby('sell_date')
    
    # stats = groups.agg(
    #     num_sold=('product', 'nunique'), 
    #     products=('product', lambda x: ','.join(sorted(set(x))))
    #     ).reset_index()

    # stats.sort_values('sell_date', inplace=True)

    # return stats
