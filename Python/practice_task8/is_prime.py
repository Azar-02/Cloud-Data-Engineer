# Write a function is_prime(n) to check if a number is prime.

# Create a module math_utils.py with two functions:
# factorial(n)
# fibonacci(n)

# Import your module and test it in another Python file.

# is_prime.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to sqrt(n)
        if n % i == 0:
            return False
    return True
