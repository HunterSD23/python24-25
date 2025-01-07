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

def sum(first, second):
    total = first + second
    print("The total of your data input is: ", total)


# Ask the user for 2 integers between 1 and 10 
a = int(input("\nPlease enter a number between one and 10: "))
b = int(input("\nPlease enter a number between one and 10: "))

myFunction(a, b)


print("\n Part 2 of our Example:\n")

# Give the user the option to repeat this process as many times as they want.
# If they want to quit, they type the word, 'Quit'.
while True:    
    # Have users input positive integers
    myVar1 = int(input("Please Enter an positive whole number: "))
    myVar2 = int(input("Please Enter an positive whole number: "))

    # call the sum() function to process the user input
    sum(myVar1, myVar2)

    print("\n\nWant to add again?\n")
    print("1. Continue")
    print("2. Quit\n")

    choice = int(input("Please type 1 or 2 to pick your choice: "))

    if choice == 2:
        print("Goodbye, come back soon! (or don't, it's fine.)\n")
        break
    else: 
        print("\nMore Math!!\n")
