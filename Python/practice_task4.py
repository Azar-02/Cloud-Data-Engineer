# Write a function that accepts a list of numbers and:
# Returns only even numbers
# Squares all odd numbers
# Saves the result to a .txt file

def process_numbers(numbers, output_file="results.txt"):
    even_numbers = [num for num in numbers if num % 2 == 0]
    squared_odds = [num ** 2 for num in numbers if num % 2 != 0]

    # Prepare output text
    output_lines = [
        "Even Numbers:\n" + ", ".join(map(str, even_numbers)),
        "\n\nSquared Odd Numbers:\n" + ", ".join(map(str, squared_odds))
    ]

    # Save to .txt file
    with open(output_file, "w") as file:
        file.write("\n".join(output_lines))

    print(f"Results saved to {output_file}")
