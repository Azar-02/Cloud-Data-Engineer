# 1. Write a program to loop through numbers 1–100:
#    - Print "Fizz" if divisible by 3
#    - Print "Buzz" if divisible by 5
#    - Print "FizzBuzz" if divisible by both

# 2. Use list comprehension to create a list of even numbers from 1 to 50.


# FizzBuzz from 1 to 100
print("=== FizzBuzz from 1 to 100 ===")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print("\n=== Even Numbers from 1 to 50 ===")
# List comprehension to get even numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print(even_numbers)
