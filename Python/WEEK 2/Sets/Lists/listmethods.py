# Create an initial list
my_list = [10, 20, 30, 40, 50]

# 1. insert() - Insert 25 at index 2
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# 2. pop() - Remove and return the last element
popped_item = my_list.pop(4)
print("After pop():", my_list, "| Popped item:", popped_item)

# 3. clear() - Remove all elements
copy_list = my_list.copy()  # Copy before clearing for later use
my_list.clear()
print("After clear():", my_list)

# 4. index() - Get index of 30
index_30 = copy_list.index(30)
print("Index of 30:", index_30)

# 5. count() - Count occurrences of 20
count_20 = copy_list.count(20)
print("Count of 20:", count_20)

# 6. sort() - Sort the list in ascending order
copy_list.sort()
print("After sort():", copy_list)

# 7. reverse() - Reverse the list
copy_list.reverse()
print("After reverse():", copy_list)

# 8. copy() - Create a copy of the list
new_list = copy_list.copy()
print("Copied list:", new_list)
