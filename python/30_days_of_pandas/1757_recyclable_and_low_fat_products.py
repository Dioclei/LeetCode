import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    is_low_fat_and_recyclable = (products["low_fats"] == 'Y') & (products["recyclable"] == "Y")
    return products[is_low_fat_and_recyclable][["product_id"]]