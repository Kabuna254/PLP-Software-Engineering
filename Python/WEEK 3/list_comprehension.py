# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# List comprehension with a condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
#even_numbers = [
#    x                  #  Expression: What gets added to the list
#    for x in range(10) #  Item & Iterable: Loops through 0-9
#    if x % 2 == 0      #  Condition: Keeps only even numbers
#]



# Create a 3x3 matrix using nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Examples of List Comprehensions
# 1.Transforming Data:
names = ["Alice", "Bob", "Charlie"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']
# 2.Filtering Data:
numbers = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)  # Output: [10, 15, 20, 25, 30]
# 3.Flattening a List:
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

# When Not to Use List Comprehensions
#- While list comprehensions are powerful, they can become hard to read if they are too complex. In such cases, traditional loops or generator functions may be more appropriate.
# Complex list comprehension (less readable)
result = [x * y for x in range(10) for y in range(5) if x + y > 5]

# Better as a loop (more readable)
result = []
for x in range(10):
    for y in range(5):
        if x + y > 5:
            result.append(x * y)


