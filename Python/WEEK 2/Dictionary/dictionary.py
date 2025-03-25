# Creating a dictionary
person = {
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles",
    "email": "alice@example.com"
}

# Printing the dictionary
print("Dictionary:", person)

# Checking the length of the dictionary
print("Length of dictionary:", len(person))

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person.get("age"))  # Using get() method

# Adding a new key-value pair
person["job"] = "Software Engineer"
print("After adding job:", person)

# Modifying a value
person["age"] = 29
print("After modifying age:", person)

# Removing a key-value pair using pop()
removed_value = person.pop("city")
print("After pop('city'):", person, "| Removed:", removed_value)

# Removing the last item using popitem()
removed_item = person.popitem()
print("After popitem():", person, "| Removed:", removed_item)

# Getting all keys
print("Keys:", person.keys())

# Getting all values
print("Values:", person.values())

# Getting all key-value pairs
print("Items:", person.items())

# Checking if a key exists
print("Is 'age' in dictionary?", "age" in person)

# Using get() method with a default value
print("Get 'email':", person.get("email"))
print("Get 'phone' (not in dictionary):", person.get("phone", "Not found"))

# Copying a dictionary
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# Updating a dictionary
person.update({"age": 30, "country": "USA"})
print("After update:", person)

# Looping through keys and values
print("Looping through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Nested dictionary (Dictionary inside a dictionary)
person["address"] = {"street": "5th Avenue", "zipcode": "10001"}
print("Nested Dictionary (Address):", person["address"])
print("Zipcode:", person["address"]["zipcode"])

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension (Squares):", squared_numbers)

# Clearing the dictionary
person.clear()
print("After clear():", person)
