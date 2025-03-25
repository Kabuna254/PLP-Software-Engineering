# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple", "orange")

# Printing the entire tuple
print("Tuple:", fruits)

# Accessing elements by index
print("First element:", fruits[0])  # apple
print("Last element:", fruits[-1])  # orange

# Slicing a tuple
print("Slice (index 1 to 3):", fruits[1:3])  # ('banana', 'cherry')

# Finding the index of an element
print("Index of 'banana':", fruits.index("banana"))

# Counting occurrences of an element
print("Count of 'apple':", fruits.count("apple"))

# Tuple unpacking
(a, b, c, d, e) = fruits
print("Unpacked values:", a, b, c, d, e)

# Looping through a tuple
print("Looping through the tuple:")
for fruit in fruits:
    print(fruit)

# Nested tuples
nested_tuple = (("John", 25), ("Jane", 30))
print("Nested Tuple:", nested_tuple)
print("Jane's Age:", nested_tuple[1][1])  # Accessing nested elements

# Immutable nature of tuples (uncommenting the next line will raise an error)
# fruits[0] = "grape"  # TypeError: 'tuple' object does not support item assignment

# Converting tuple to list (to modify it)
fruits_list = list(fruits)
fruits_list.append("grape")  # Adding an element
print("Modified List:", fruits_list)

# Converting list back to tuple
new_fruits_tuple = tuple(fruits_list)
print("New Tuple:", new_fruits_tuple)
