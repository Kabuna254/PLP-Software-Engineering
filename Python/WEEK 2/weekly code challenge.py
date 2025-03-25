# Sum of integers in a list
numbers = [int(x) for x in input("Enter integers separated by space: ").split()]
print("Sum of the integers:", sum(numbers))

# Tuple of favorite books
favorite_books = ("Rich Dad Poor Dad", "To Kill a Mockingbird", "The Holy Bible", "The 48 Laws of Power", "Caucasian Chalk Circle")
print("\nFavorite Books:")
for book in favorite_books:
    print(book)

# Dictionary storing user information
person = {}
person["name"] = input("\nEnter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")
print("\nPerson Info:", person)

# Intersection of two sets
# Taking user input for the first set, splitting by space, and converting to a set of integers
set1 = {int(x) for x in input("\nEnter first set of integers separated by space: ").split()}
# Taking user input for the second set, splitting by space, and converting to a set of integers
set2 = {int(x) for x in input("Enter second set of integers separated by space: ").split()}
# Finding the common elements using the intersection (&) operator
common_elements = set1 & set2  
# Printing the common elements
print("Common elements:", common_elements)


# List comprehension for odd-length words
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("\nWords with odd number of characters:", odd_length_words)
