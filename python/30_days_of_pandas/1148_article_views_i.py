import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    articles_viewed_by_their_author = views[views['author_id'] == views['viewer_id']]
    authors = articles_viewed_by_their_author['author_id'].drop_duplicates().sort_values()
    return pd.DataFrame({'id': authors})