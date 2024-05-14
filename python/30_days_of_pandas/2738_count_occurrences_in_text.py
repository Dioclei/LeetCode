import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    files['has_bull'] = files['content'].str.contains(r'\sbull\s', case=False).astype(int)
    files['has_bear'] = files['content'].str.contains(r'\sbear\s', case=False).astype(int)
    print(files)
    total_bull_count = files['has_bull'].sum()
    total_bear_count = files['has_bear'].sum()
    return pd.DataFrame({'word': ['bull', 'bear'], 'count': [total_bull_count, total_bear_count]})
