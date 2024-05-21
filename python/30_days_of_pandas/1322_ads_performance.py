import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    v_count = ads[ads['action'] != 'Ignored'].groupby('ad_id').size().reset_index(name='view_count')
    c_count = ads[ads['action'] == 'Clicked'].groupby('ad_id').size().reset_index(name='click_count')
    count = pd.merge(v_count, c_count, on='ad_id', how='left')
    count = pd.merge(ads[['ad_id']].drop_duplicates(), count, on='ad_id', how='left')
    count['ctr'] = count['click_count'] / count['view_count'] * 100
    count['ctr'] = count['ctr'].fillna(0)
    count['ctr'] = count['ctr'].round(2)
    count = count.sort_values(['ctr', 'ad_id'], ascending=[False, True])
    return count[['ad_id', 'ctr']]

    # editorial answer is a bit more literal, using apply to apply the ctr formula
    # Group by 'ad_id' and calculate the CTR for each group
    ctr = ads.groupby('ad_id')['action'].apply(
        lambda x: round(
            (sum(x == 'Clicked') / (sum(x == 'Clicked') + sum(x == 'Viewed')) * 100) if (sum(x == 'Clicked') + sum(x == 'Viewed')) > 0 else 0.00, 
            2
        )
    ).reset_index()

    # Rename the column to 'ctr'
    ctr.columns = ['ad_id', 'ctr']
    
    # Sort the results by 'ctr' in descending order and by 'ad_id' in ascending order
    result = ctr.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])

    return result