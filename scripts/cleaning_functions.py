import pandas as pd

def convert_date_columns(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

def drop_unwanted_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop)

def fill_missing_values(df, fill_rules):
    for col, value in fill_rules.items():
        df[col] = df[col].fillna(value)
    return df
