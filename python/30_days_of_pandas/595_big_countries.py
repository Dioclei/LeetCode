import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area_is_big = world.loc[:, "area"] >= 3000000
    pop_is_big = world.loc[:, "population"] >= 25000000
    is_big = area_is_big | pop_is_big
    return world[is_big].loc[:, ["name", "population", "area"]]