"""
Program: counting.py
Author: Hunter Dettmer
"""

print("Using the continue Statement in a Loop.")
print("--------------------------------------")

currentNumber = 0 

while currentNumber < 10: 

    currentNumber += 1 # Control Variable
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)