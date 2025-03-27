# Syntax:
def function_name(parameters):
    """Optional docstring explaining the function."""
    # Code block
    return value  # Optional return statement


# Defining and calling a function
# Function definition
def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))  # Output: Hello, Alice!

# 1.Positional Arguments:
def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8
# 2.Keyword Arguments:
def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))  # Output: My name is Bob, and I'm 25 years old.
# 3.Default Arguments:
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

# Returning values
# A function can return values using the return statement. 
def square(number):
    return number ** 2

result = square(4)
print(result)  # Output: 16

# Anonymous Functions: Lambda
# Lambda functions are small anonymous functions that can take any number of arguments, but can only have one
# Lambda function for adding two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
# Using lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# Recursive Functions
# A function that calls itself is called a recursive function.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# LAMBDA AND DEF COMPARISONS TO PRINT SAME OUTPUT
# Using lambda
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8

# Using def
def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8
