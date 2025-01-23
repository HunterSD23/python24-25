"""
This program takes integers from a user and sums the numbers up. If the user inputs a string or special characters, the program will still add the numbers together, but anything other than an integer will be skipped and replaced with a zero. (the program should also let the user know when the input they entered was skipped and why.)
"""

def add_all_num():

    try:
        num_one = int(input("Enter an integer: "))
    except ValueError:
        print("\nError: You have entered a string or character that is not an integer and therefore the number has been skipped. The program will continue.\n")
        num_one = 0

    try:
        num_two = int(input("Enter an integer: "))
    except ValueError:
        print("\nError: You have entered a string or character that is not an integer and therefore the number has been skipped. The program will continue.\n")
        num_two = 0

    try:
        num_three = int(input("Enter an integer: "))
    except ValueError:
        print("\nError: You have entered a string or character that is not an integer and therefore the number has been skipped. The program will continue.\n")
        num_three = 0

    try:
        num_four = int(input("Enter an integer: "))
    except ValueError:
        print("\nError: You have entered a string or character that is not an integer and therefore the number has been skipped. The program will continue.\n")
        num_four = 0

    try:
        num_five = int(input("Enter an integer: "))
    except ValueError:
        print("\nError: You have entered a string or a character that is not an integer and therefore the number has been skipped. The program will continue.\n")
        num_five = 0

    print("\nThe program will now take your numbers and find the sum. . .")
    sum = num_one + num_two + num_three + num_four + num_five

    print(f"\n\nThe sum of {num_one, num_two, num_three, num_four, num_five}, is {sum}.\n")

add_all_num()