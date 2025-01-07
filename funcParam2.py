'''

This program will accept 2 inputs from the user and process the data as exoponents of one another.
'''
# This function prints the user inputs and then calculates them as exponents of one another and prints them out to the terminal window
def myFunction(a, b):
    print("\nVariable a is: ", a, ".")
    print("\nVariable b is: ", b, ".")
    exp1 = a ** b
    exp2 = b ** a
    print("\n", a, " to the power of ", b, "is: ", exp1)
    print("\n", b, " to the power of ", a, "is: ", exp2)


# Ask the user for 2 integers between 1 and 10 
a = int(input("\nPlease enter a number between one and 10: "))
b = int(input("\nPlease enter a number between one and 10: "))

myFunction(a, b)