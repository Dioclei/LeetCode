import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # question deals with string validation, so we should use regex
    return patients[patients['conditions'].str.contains(r'($|\s)DIAB1')]