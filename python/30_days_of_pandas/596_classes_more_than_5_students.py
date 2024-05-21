import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_size = courses.groupby('class').size().reset_index(name='class_size')
    return class_size[class_size['class_size'] >= 5][['class']]