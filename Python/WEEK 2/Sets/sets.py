# Creating sets
fruits = {"apple", "banana", "cherry"}
more_fruits = {"banana", "orange", "grape"}

print("Initial Sets:")
print("Fruits:", fruits)
print("More Fruits:", more_fruits)

# Adding elements
fruits.add("mango")
print("\nAfter adding 'mango':", fruits)

# Removing elements
fruits.remove("banana")  # Raises an error if item is not found
print("After removing 'banana':", fruits)

# Using discard (won't raise error if not found)
fruits.discard("pineapple")

# Checking membership
print("\nIs 'apple' in fruits?", "apple" in fruits)

# Set Union (combining two sets)
all_fruits = fruits.union(more_fruits)
print("\nUnion of both sets:", all_fruits)

# Set Intersection (common elements)
common_fruits = fruits.intersection(more_fruits)
print("Intersection (common elements):", common_fruits)

# Set Difference (elements in one set but not the other)
unique_fruits = fruits.difference(more_fruits)
print("Difference (unique to 'fruits'):", unique_fruits)

# Set Symmetric Difference (elements in either set, but not both)
sym_diff = fruits.symmetric_difference(more_fruits)
print("Symmetric Difference:", sym_diff)

# Checking subset and superset
print("\nIs 'fruits' a subset of 'all_fruits'?", fruits.issubset(all_fruits))
print("Is 'all_fruits' a superset of 'fruits'?", all_fruits.issuperset(fruits))

# Converting list to set (removes duplicates)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\nList converted to set (duplicates removed):", unique_numbers)

# Converting list to set (removes duplicates)
numbers = {1, 2, 2, 3, 4, 4, 5}
more_numbers = {3, 4, 5, 6, 7}

print("\nNumbers Set:", numbers)
print("More Numbers Set:", more_numbers)

# Union ( | ) - Combines elements from both sets
print("\nUnion:", numbers | more_numbers)

# Intersection ( & ) - Common elements in both sets
print("Intersection:", numbers & more_numbers)

# Difference ( - ) - Elements in first set but not in second
print("Difference (Numbers - More Numbers):", numbers - more_numbers)

# Symmetric Difference ( ^ ) - Elements in either set, but not both
print("Symmetric Difference:", numbers ^ more_numbers)

set1 = {1, 2, 3, 4, 5}
set2 = {5, 4, 3, 2, 1}
set3 = {1, 2, 3}

print(set1 == set2)  # True (same elements)
print(set1 == set3)  # False (set3 is missing elements)