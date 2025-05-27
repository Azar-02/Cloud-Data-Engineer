# Write a Python program to Create a dictionary of products & their prices

# products = {
#     "Laptop": 85000,
#     "Phone": 45000,
#     "Tablet": 30000,
#     "Monitor": 15000,
#     "Keyboard": 2500
# }

# Print the most expensive and the cheapest product
# Calculate and print the total value of all products
# Find and print all products priced above ₹30,000
# 🔁 BONUS Challenge (Optional):
# Allow the user to input a minimum price, and list all products above that price.


# 1. Dictionary of products and their prices
products = {
    "Laptop": 85000,
    "Phone": 45000,
    "Tablet": 30000,
    "Monitor": 15000,
    "Keyboard": 2500
}

# 2. Find the most expensive and cheapest product
most_expensive = max(products, key=products.get)
cheapest = min(products, key=products.get)

print(f"Most Expensive Product: {most_expensive} (₹{products[most_expensive]})")
print(f"Cheapest Product: {cheapest} (₹{products[cheapest]})")

# 3. Calculate total value of all products
total_value = sum(products.values())
print(f"\nTotal Value of All Products: ₹{total_value}")

# 4. Find and print all products priced above ₹30,000
print("\nProducts priced above ₹30,000:")
for name, price in products.items():
    if price > 30000:
        print(f"- {name}: ₹{price}")

# BONUS: User-defined price filter
min_price = int(input("\nEnter a minimum price to filter products: ₹"))
print(f"Products above ₹{min_price}:")
for name, price in products.items():
    if price > min_price:
        print(f"- {name}: ₹{price}")
