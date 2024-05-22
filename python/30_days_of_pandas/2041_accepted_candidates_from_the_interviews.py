import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    # join rounds and candidates
    df = pd.merge(rounds, candidates, how='left', on='interview_id')
    # at least 2 years of interview
    df = df[df['years_of_exp'] >= 2]
    # sum of score of interview rounds is > 15
    candidate_ids = df.groupby('candidate_id')['score'].sum().reset_index(name='score')
    return candidate_ids[candidate_ids['score'] > 15]['candidate_id']

    # Notes:
    # would probably be a little faster if I filter out the candidates and rounds first, then take an inner join
    # as opposed to joining everything at the start and then filtering.