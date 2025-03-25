# A list of three numbers
numbers = [1, 2, 3]
print(numbers)

# empty list
my_list = []
print(my_list)

# list with mixed data types
my_list = [1, "Hello", 3.4] # int, str, float
print(my_list)

languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[0]) # Python
# access item at index 2
print(languages[2]) # C++

# List slicing in Python
print(languages[-1]) # C++
my_list = ['p', 'r', 'o', 'g', 'r', 'a','m', 'i']
# items from index 2 to 4
print (my_list[2:5]) # ['o', 'g', 'r']
# items from index 5 to end
print(my_list[5:])
# items from beginning to end
print(my_list[:])
# access item at index 2
print(languages[-3]) # Python

# Adding elements to a list
numbers = [21, 34, 54, 12]
print("Before Append: ", numbers)
# using append method
numbers.append(32)
print("After append: ", numbers)
# using extend method
prime_numbers = [2, 3, 5]
print("List1: ", prime_numbers)
even_numbers = [4, 6, 8]
print("List2: ", even_numbers)
# Join two lists
prime_numbers.extend(even_numbers)
print("List after extend: ", prime_numbers)

# Change list items
languages[2] = "C"
print(languages)