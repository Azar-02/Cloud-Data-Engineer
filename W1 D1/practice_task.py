# hello_data_engineer.py

from datetime import date
import pandas as pd

# Print your name and today's date

my_name = "Arc"  # Replace with your actual name
today = date.today()
print(f"Name: {my_name}")
print(f"Date: {today}")

# from datetime import date: Imports the date class from Python’s built-in datetime module.
# today = date.today(): Gets the current date.
# print(...): Displays your name and the current date using formatted strings (f-strings).


# Sample dictionary

data = {
    "Name": ["Alice", "Bob", "Charles"],
    "Age": [19, 25, 38],
    "City": ["New York", "Paris", "London"]
}
print("\nSample Dictionary:")
print(data)

# data = {...}: Creates a Python dictionary with 3 keys (Name, Age, City) and list values.
# print(...): Displays the dictionary on the screen.



# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
print("\nDictionary has been written to 'sample_data.csv'")

# import pandas as pd: Imports the pandas library and shortens the name to pd.
# pd.DataFrame(data): Converts the dictionary to a DataFrame (a table-like structure).
# to_csv("sample_data.csv", index=False): Saves the DataFrame to a file named sample_data.csv 
# without writing row numbers (index).
# print(...): Confirms the file has been created.


