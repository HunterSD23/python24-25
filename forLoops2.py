"""
Author: Hunter Dettmer
Program: forLoops2.py
Last Update: 9/25/2024
"""
for blah in range(5):
    print("Blah blah blah", end = " SPACE ")

print("This is outside of the for Loop.")

print() #empty print statement adds a blank line
print() #it works like a <br> in HTML 

print("Using Outside variables in a for Loop")
print("---------------------------------------")

# Instantiating our variables 
number = 5 
exponent = 4 
product = 1 

# Create a for Loop to find the value of our number to the exponent
for eachPass in range(exponent):
    product = product * number
    print(product, end = " ")
print("\n") # \n is a character to create a New Line (<br>)

print(product) # 625

print("\n\n\nCount-Controlled Loops")
print("---------------------------------------\n\n")

for count in range(4):
    print(count, end = " - ")
print()

print("Off-by-one error occurs because default counting always starts at 0.")

print("\nOff-by-one correction")
print("---------------------------------------\n")
product = 1 

for count in range(4):
    product = product * (count + 1)
print(product)


print("\n\nUsing Lower & Upper Bounds")
print("---------------------------------------")

product = 1

for count in range(1, 5):
    product = product * count

print(product)

print("\n\nSummation using Lower & Upper Bounds")
print("---------------------------------------")

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

theSum = 0

for number in range(lower, upper + 1):
    theSum += number

print("The summation of ", lower, "to ", upper, "is: ", theSum)