# 1. Create a list of names, remove duplicates using set.
# 2. Convert it back to a sorted list.
# 3. Store each name with an ID in a dictionary and print key-value pairs.

# 1. Create a list of names with duplicates
names = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]

# Remove duplicates using a set
unique_names = set(names)

# 2. Convert the set back to a sorted list
sorted_names = sorted(unique_names)

# 3. Store each name with an ID in a dictionary
# We'll use ID starting from 1
name_dict = {i + 1: name for i, name in enumerate(sorted_names)}

# Print key-value pairs
print("ID -> Name")
for id, name in name_dict.items():
    print(f"{id} -> {name}")
