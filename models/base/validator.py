
def validate_dataframe(df,target):
    if df.empty:
        raise ValueError("Empty dataset")
    if target not in df.columns:
        raise ValueError("Missing target")
    return True
