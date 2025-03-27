# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it. 

def alphabet_position(text):
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())

#Explanation
#Convert to lowercase: text.lower() ensures case insensitivity.
#Iterate over characters: for char in text
#Check if it's a letter: if char.isalpha()
#Find its position in the alphabet:
#ord(char) - 96 gives the letter's position ('a' = 1, 'b' = 2, etc.)
#Join the numbers into a string: " ".join(...) creates a single output string.