"""
Positional Arguments: Arguments are passed in order.
Keyword Arguments: Arguments are passed using their name.

✅ Algorithm
Define a function with one or more parameters.
Assign default values to parameters that can be optional.
Call the function using positional or keyword arguments.

✅ Pseudocode
DEFINE function_name(param1, param2=default_value):
    PERFORM some task
    RETURN result
CALL function_name(value1)  # Uses default for param2
CALL function_name(value1, value2)  # Overrides default
"""

# BQ1: Write a function describe_pet(name, animal="dog") that prints a message about the pet.
def describe_pet(name, animal):
    return f"{name} is a {animal}"
print(describe_pet("Blondie", "cat"))

# BQ2:Write a function greet_user(name, greeting) that returns a greeting message.
def greet_user(greeting, name):
    return f"{greeting} {name}"
print(greet_user("Good Morning", "Mr. Omereife!"))

# BQ3: Write a function multiply(a, b=2) that multiplies two numbers (default second number is 2).
def multiply(a, b=2):
    return  a * 2
print(multiply(6, 2))

# Intermediate Exercises:
#Q1 Modify multiply(a, b=2) so that it also accepts a keyword argument power=2, which raises the result to a power.

def multiply(a, b=2):
    return  (a * 2)**2
print((multiply(4 , 2))**2)

#Q2 Write a function calculate_area(length, width=10), where width has a default value.
def calculate_area(length, width=10):
    return length * 10
print(calculate_area(18 , 10))

# Q3 Create a function format_date(day, month, year=2024) that prints a formatted date, using 2024 as the default year.
def format_date(day, month, year=2024):
    return f"{day}-{month}-2024"
print(format_date(16,11,2024))