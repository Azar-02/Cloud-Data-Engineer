import pandas as pd
import math

def load_data(filepath):
    return pd.read_csv(filepath)

def get_total_cases(df, country):
    row = df[df["Country"] == country]
    if not row.empty:
        return int(row.iloc[0]["TotalCases"])
    return None

def get_death_rate(df, country):
    row = df[df["Country"] == country]
    if not row.empty:
        cases = row.iloc[0]["TotalCases"]
        deaths = row.iloc[0]["TotalDeaths"]
        if cases > 0:
            return round((deaths / cases) * 100, 2)
    return None

def get_countries_above_threshold(df, threshold):
    return df[df["TotalCases"] > threshold]["Country"].tolist()
