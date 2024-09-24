"""
Simple for Loop Statement
"""
for eachPass in range(5):
    print("It's a-Me!", end = " ") # Empty string to create a blank space
    print("This print statement is still part of the for Loop")

print("This print statement is outside of our for loop")

print()
print()
print()

"""
Using Variables with for Loops
"""
print("Using Variables with for Loops")
print("----------------------------------------")
number = 2
exponent = 3
product = 1

for eachPass in range(exponent): # for eachPass in range(3):
    product = product * number # Reassigning the value of the product variable
    print(product, end = " \n") # \n creates a line break

"""
Controlling for Loops with a Count
"""

print("\n\n\nControlling for Loops with a Count")
print("----------------------------------------")

for count in range(7):
    print(count, end=" ")

print("\n\n")

product = 1
for count in range(4): # The count variable will start at 0 and auto-increment
    product = product * (count + 1) # Off by-1 Error fix

print(product)

print("\n\n\n")

"""
Using 2 numbers in your range
"""
print("Using 2 numbers in your range")
print("----------------------------------------")

product = 1
for count in range(1, 5):
    product = product * count # No longer have an off by-1 error

print(product)