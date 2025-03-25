# Creating a string
text = "  Hello, Python! Welcome to string methods.  "

# Printing the original string
print("Original String:", text)

# String Length
print("Length of String:", len(text))

# Converting to Uppercase and Lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Swapping Case
print("Swapped Case:", text.swapcase())

# Checking if String is in Title Case
print("Is title case?", text.istitle())

# Centering the Text
print("Centered String:", text.center(50, "-"))

# Removing Whitespaces
print("Stripped (removing spaces from start and end):", text.strip())

# Checking if String Starts or Ends with a Specific Substring
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with '.':", text.endswith("."))

# Finding a Substring
print("Index of 'Python':", text.find("Python"))  # Returns -1 if not found

# Replacing Substrings
print("Replacing 'Python' with 'World':", text.replace("Python", "World"))

# Splitting a String into a List
words = text.split()
print("Splitting into words:", words)

# Joining a List into a String
new_text = "-".join(words)
print("Joining words with '-':", new_text)

# Checking if String is Numeric
num_str = "12345"
print("Is '12345' numeric?", num_str.isnumeric())

# Checking if String is Alphabetic
alpha_str = "Hello"
print("Is 'Hello' alphabetic?", alpha_str.isalpha())

# Checking if String is Alphanumeric
alnum_str = "Hello123"
print("Is 'Hello123' alphanumeric?", alnum_str.isalnum())

# Checking if String Contains Only Spaces
print("Is the string only spaces?", text.isspace())

# Counting Occurrences of a Substring
print("Occurrences of 'o':", text.count("o"))

# Accessing Characters in a String (Indexing)
print("First character:", text[0])
print("Last character:", text[-1])

# String Slicing
print("Slice (first 5 chars):", text[:5])
print("Slice (last 7 chars):", text[-7:])

# Reversing a String
print("Reversed String:", text[::-1])

# Formatting Strings (f-strings)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Checking if a String Contains a Word
print("Is 'Python' in text?", "Python" in text)

# Expanding Tabs
tab_text = "Hello\tPython"
print("Expanded Tabs:", tab_text.expandtabs(4))

# Iterating Through the String
print("Iterating through characters:")
for char in text:
    print(char, end=" ")  # Prints each character with a space in between
print()

# Creating a string
text = "  Hello, Python! Welcome to string methods.  "

# Splitting the string into words
words = text.split()

# Iterating through words instead of characters
print("Iterating through words:")
for word in words:
    print(word)