import numpy as np

# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)

# Perform operations
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Average of the array
print("Square Roots:", np.sqrt(my_array))

import numpy as np

# Create an array with numbers from 10 to 50 (inclusive)
arr = np.arange(10, 51)
print("Original array:", arr)

# Find maximum and minimum values
max_val = np.max(arr)
min_val = np.min(arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

# Multiply all elements by 3
arr_times_3 = arr * 3
print("Array multiplied by 3:", arr_times_3)
