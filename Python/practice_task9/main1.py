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

from covid_utils import load_data, get_total_cases, get_death_rate, get_countries_above_threshold

def main():
    filepath = "covid_data.csv"
    df = load_data(filepath)

    while True:
        print("\n📊 COVID-19 Data Summary Tool")
        print("1. Total cases by country")
        print("2. Death rate by country")
        print("3. Countries with cases above threshold")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            country = input("Enter country name: ")
            total = get_total_cases(df, country)
            print(f"Total cases in {country}: {total if total else 'Not found'}")

        elif choice == "2":
            country = input("Enter country name: ")
            rate = get_death_rate(df, country)
            print(f"Death rate in {country}: {rate}%") if rate else print("Data not found.")

        elif choice == "3":
            threshold = int(input("Enter case threshold: "))
            countries = get_countries_above_threshold(df, threshold)
            print("Countries with cases above threshold:", countries)

        elif choice == "4":
            print("Exiting... Stay safe! 😷")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
