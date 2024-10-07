"""
Program: reviewChallengeOne.py
Author: Hunter Dettmer
"""

numberone = int(input("Please enter a number: "))
operation = input("Please enter the operation you would like to use in word form: ")
numbertwo = int(input("Please enter another number: "))

if operation == "plus":
    answer = numberone + numbertwo
elif operation == "minus":
    answer = numberone - numbertwo
elif operation == "times":
    answer = numberone * numbertwo
elif operation == "divide":
    answer = numberone / numbertwo
else:
    answer = print("You have given an invalid operation")
print("\n")
if answer == print("You have given an invalid operation"):
    print("Please try entering an operation like 'plus' or 'minus'")
else:    
    print("The solution to", numberone, operation, numbertwo, "is...", answer)