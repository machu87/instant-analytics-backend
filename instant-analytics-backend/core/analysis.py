import pandas as pd
import io

def dataframe_from_upload(file_bytes: bytes, filename: str) -> pd.DataFrame:
    if filename.lower().endswith('.csv'):
        return pd.read_csv(io.BytesIO(file_bytes))
    return pd.read_excel(io.BytesIO(file_bytes))

def build_schema_summary(df: pd.DataFrame) -> dict:
    info = {
        "columns": [
            {"name": c, "dtype": str(df[c].dtype), "nulls": int(df[c].isna().sum())}
            for c in df.columns
        ],
        "shape": {"rows": int(df.shape[0]), "cols": int(df.shape[1])},
        "describe_numeric": df.describe(include='number').round(4).to_dict()
    }
    cat_cols = [c for c in df.columns if df[c].dtype == 'object']
    topcats = {c: df[c].value_counts(dropna=True).head(10).to_dict() for c in cat_cols}
    info["top_categories"] = topcats
    return info

def aggregate_for_chart(df: pd.DataFrame, params: dict) -> list[dict]:
    x = params.get("x_axis")
    y = params.get("y_axis")
    group = params.get("group_by")
    agg = params.get("agg","sum")
    if x and y and group:
        g = df.groupby([x, group])[y].agg(agg).reset_index()
        return g.to_dict(orient='records')
    if x and y:
        g = df.groupby(x)[y].agg(agg).reset_index()
        return g.to_dict(orient='records')
    return df.head(100).to_dict(orient='records')
