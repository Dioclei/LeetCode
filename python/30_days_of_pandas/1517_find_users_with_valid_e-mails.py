import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.fullmatch('[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com')]

    # editorial regex, note the use of raw strings, escaping @, and using ^ and $ to indicate start and end of string, instead of using fullmatch
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]