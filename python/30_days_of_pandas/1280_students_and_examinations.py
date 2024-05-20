import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    attended_exams_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    df = pd.merge(students.sort_values('student_id'), subjects.sort_values('subject_name'), how='cross')
    df = pd.merge(df, attended_exams_count, on=['student_id', 'subject_name'], how='left')
    df['attended_exams'] = df['attended_exams'].fillna(0)
    df = df[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    return df
