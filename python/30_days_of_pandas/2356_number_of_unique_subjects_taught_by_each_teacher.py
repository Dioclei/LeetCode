import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # basically dept_id doesn't matter
    # obtain unique subjects for each teacher
    df = teacher[['teacher_id', 'subject_id']].drop_duplicates()
    # count number of subjects for each teacher
    count = df.groupby(['teacher_id']).size().reset_index(name='cnt')
    return count[['teacher_id', 'cnt']]

    # one-liner with nunique
    return teacher.groupby(["teacher_id"])["subject_id"].nunique().reset_index(name='cnt')