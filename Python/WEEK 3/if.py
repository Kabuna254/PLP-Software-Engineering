# Get the grade input from the user
grade = int(input("Enter your grade: "))

# Check the grade and assign the letter grade
if grade > 100:
    print("Error")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade > 0:
    print("F")
else:
    print("Error")

# Ask the user if they are hungry
hungry = input("Are you hungry? (yes/no): ").strip().lower() # .strip().lower() Removes extra spaces and converts input to lowercase.

# Check the response and print the appropriate message
if hungry == "yes":
    print("You should eat some food!")
elif hungry == "no":
    print("You're good for the day!")
else:
    print("Please enter 'yes' or 'no'.")

