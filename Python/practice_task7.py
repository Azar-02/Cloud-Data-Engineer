# Loop through numbers from 1 to 100
# Count how many times:
# "Fizz" appears (divisible by 3 only)
# "Buzz" appears (divisible by 5 only)
# "FizzBuzz" appears (divisible by both)
# Print the counts at the end

# === Challenge 1: Fizz Count ===
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif num % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif num % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(num)

# Print summary
print("\n=== Fizz Count Summary ===")
print(f"Fizz: {fizz_count} times")
print(f"Buzz: {buzz_count} times")
print(f"FizzBuzz: {fizzbuzz_count} times")


# === Challenge 2: Squares of Multiples of 3 from 1 to 50 ===
squares_of_multiples_of_3 = [num**2 for num in range(1, 51) if num % 3 == 0]

print("\n=== Squares of Multiples of 3 (1–50) ===")
print(squares_of_multiples_of_3)
