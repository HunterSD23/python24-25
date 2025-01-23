"""
This program tries to recieve an integer from a user. If the user enters something other than an integer, the program handles it by printing an error.
"""
try:
    my_number = int(input("Enter an integer: "))
    print("Your number: " + str(my_number))
except ValueError:
    print("That wasn't an integer you nitwit!")

print("See... the program is still running.")