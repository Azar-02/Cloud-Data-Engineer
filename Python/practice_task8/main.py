# main.py

from is_prime import is_prime
import math_utils

# Test is_prime
print("Is 7 prime?", is_prime(7))   # True
print("Is 10 prime?", is_prime(10)) # False

# Test factorial
print("Factorial of 5:", math_utils.factorial(5))  # 120

# Test fibonacci
print("First 7 Fibonacci numbers:", math_utils.fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
