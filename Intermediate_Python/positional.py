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

