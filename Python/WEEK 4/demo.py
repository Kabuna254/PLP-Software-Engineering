# Step 1: Read the contents of input.txt
with open('Python\WEEK 4\input.txt', 'r') as f:
    content = f.read()

# Step 2: Count the number of words in the file
words = content.split()  # Splits the content by whitespace into a list of words
word_count = len(words)

# Step 3: Convert all text to uppercase
uppercase_content = content.upper()

# Step 4: Write the processed text and word count to a new file called output.txt
with open('Python\WEEK 4\output.txt', 'w') as f:
    f.write("Processed Text (Uppercase):\n")
    f.write(uppercase_content + "\n\n")
    f.write("Word Count: " + str(word_count))

# Step 5: Print a success message
print("The new file 'output.txt' has been created with the processed content and word count.")
