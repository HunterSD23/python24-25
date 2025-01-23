"""
This program asks the user for their name and age. It handles the case where the user fails to enter a valid integer for their age.
"""

name = input("Please enter your first name: ")
age = -1

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("That wasn't an integer! Mr. " + name)


# Print name and age, using default age if user did not enter an integer
print("Name: " + name)

if age == -1:
    try:
        age = int(input("Please re-enter your age: "))
    except ValueError:
        print("WHAT IS WRONG WITH YOU?? That wasn't an integer! Mr. " + name)
        age = "I give up!!"

print("Age: " + str(age))