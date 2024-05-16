import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # can use size()
    # cnts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    # return cnts[cnts['counts'] >= 3][['actor_id', 'director_id']]

    df = actor_director.groupby(['actor_id', 'director_id']).count()
    return df[df['timestamp'] >= 3].reset_index()[['actor_id', 'director_id']]

