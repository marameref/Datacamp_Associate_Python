# pseudocade:
""" 
DEFINE function_name(parameter):
    PERFORM the required task
    RETURN the result
CALL function_name(input_value)
"""
# Write a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b

print(add_numbers(5,6))

# Write a function greet_user(name) that prints "Hello, name!".
def greet_user(name):
    return f"Hello, {name}"
print(greet_user("Amara"))

#Write a function square(n) that returns the square of a number.
def square(n):
    return n**2
print(square(7))

# Write a function is_even(n) that returns True if a number is even and False otherwise.
def is_even(n):
    return n % 2 == 0

print(is_even(3))

# Write a function find_max(a, b, c) that returns the largest of three numbers.
def find_max(a, b, c):
    return max(a,b,c)
print(find_max(6,9,12))

# Write a function reverse_string(s) that returns the reverse of a given string.
def reverse_string(s):
    return s[::-1]
print(reverse_string('Stanley'))