from typing import Dict
import pandas as pd
import uuid

_DATAFRAMES: Dict[str, pd.DataFrame] = {}

def save_dataframe(df: pd.DataFrame) -> str:
    key = str(uuid.uuid4())
    _DATAFRAMES[key] = df
    return key

def get_dataframe(key: str) -> pd.DataFrame:
    return _DATAFRAMES[key]
