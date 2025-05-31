# 🛠️ Mini Project – COVID-19 Data Summary Tool
# Create a Python script that:
# Loads a sample COVID-19 dataset (CSV)
# Calculates stats like total cases, deaths by country
# Filters data by country and shows summary
# Uses functions and modules for code reuse

# Tasks:
# Load CSV using csv or pandas
# Extract column headers
# Write functions:
# get_total_cases(country)
# get_death_rate(country)
# get_countries_above_threshold(threshold)
# Use conditionals and loops
# Use math module for rounding, etc.
# 🔗 Optional Tools:
# Try pandas for better data handling (install with pip install pandas)
# Use a CLI input (input()) to make it interactive

import pandas as pd
import math
from covid_utils import load_data, get_total_cases, get_death_rate, get_countries_above_threshold

# Load CSV with pandas
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("✅ Data loaded successfully!")
        print("📋 Columns:", list(df.columns))
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return pd.DataFrame()

# Get total cases for a given country
def get_total_cases(df, country):
    row = df[df["Country"] == country]
    if not row.empty:
        return int(row.iloc[0]["TotalCases"])
    return None

# Get death rate as a percentage
def get_death_rate(df, country):
    row = df[df["Country"] == country]
    if not row.empty:
        cases = row.iloc[0]["TotalCases"]
        deaths = row.iloc[0]["TotalDeaths"]
        if cases > 0:
            return round((deaths / cases) * 100, 2)
    return None

# Get countries with cases above a threshold
def get_countries_above_threshold(df, threshold):
    return df[df["TotalCases"] > threshold]["Country"].tolist()
