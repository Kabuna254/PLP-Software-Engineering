languages = ["Python", "Swift", "C++", "C", "Java", "R"]
# deleting the second item
del languages[1]
print(languages)
# deleting the last item
del languages[-1]
print(languages)
# deleting first two items
del languages[0:2]
print(languages)

# Using remove
languages = ["Python", "Swift", "C++", "C", "Java", "R"]
# remove Python from the list
languages.remove("Python")
print(languages)
