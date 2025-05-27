# Simple Practice Task
# Write a Python script to:
# Print your name and today’s date
# Load a sample dictionary and print it
# Write the dictionary to a CSV file using pandas


from datetime import date
import pandas as pd

# Print your name and today's date
my_name = "Arc"  # Replace with your actual name
today = date.today()
print(f"Name: {my_name}")
print(f"Date: {today}")


# Sample dictionary
data = {
    "Name": ["Alice", "Bob", "Charles"],
    "Age": [19, 25, 38],
    "City": ["New York", "Paris", "London"]
}
print("\nSample Dictionary:")
print(data)

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
print("\nDictionary has been written to 'sample_data.csv'")