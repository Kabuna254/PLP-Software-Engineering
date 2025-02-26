#Variables hold data
age = 25 #int (integer)
height = 5.75 #float (decimal number)
name = "Charlie" #str (string)
is_student = True #bool (boolean)

#Printing out the values
print("Name: ", name) #outputs: Name: Charlie
print("Age: ", age) #outputs: Age: 25
print("Height: ", height) #outputs: Height: 5.75
print("Is a student?", is_student) #outputs: Is a student? True

#Making decisions
temperature = int(input("Enter temperature: "))

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's a cool day!")

#Control flow example for grading student marks
#This will ask the user for input and grade the student's performance
#Prompt the user for student marks
marks = int(input("Enter the student's marks: "))
#Grading system based on the marks
if 79 <= marks <= 100:
    print("Grade: A")
elif 69 <= marks <= 78:
    print("Grade: B")
elif 59 <= marks <= 68:
    print("Grade: C")
elif 49 <= marks <= 58:
    print("Grade: D")
elif 39 <= marks <= 48:
    print("Fail")
else:
    print("ERROR")
