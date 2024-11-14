print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero

# Write an if/else (elif) structure to determine the number's positive, negative, zero state
number = int(input("Enter any whole number: "))

if number == 0:
    print("The number is zero")
elif number < 0:
    print("The number is a negative")
else:
    print("The number is a positive")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = input("Enter your username: ") # "admin"

# Write your Code Below

if user_role == "admin":
    print("You have administrator privileges!")
else:
    print("You do not have administrator privileges.")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
year = int(input("Enter a year to see if it is a leap year: "))

# Write your Code Below

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is NOT a leap year.")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = int(input("Enter your age to get classified into an age group: "))

# Write your Code Below

if age >= 90:
    print("You are in your 90's and are old news.")
elif age >= 80:
    print("You are in your 80's and are probably a boomer.")
elif age >= 70:
    print("You are in your 70's and are a boomer.")
elif age >= 60:
    print("You are in your 60's and classified as old.")
elif age >= 50:
    print("You are in your 50's and getting old.")
elif age >= 40:
    print("You are in your 40's.")
elif age >= 30:
    print("You are in your 30's.")
elif age >= 20:
    print("You are in your 20's.")
elif age >= 10:
    print("You are in your 10's.")
elif age >= 0:
    print("How is a baby even giving an answer??")
else:
    print("Error: You have entered an age younger than 0.")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = int(input("Enter the amount of the purchase: "))

# Write your code Below
if purchase_amount >= 100:
    discount = .20
    amount_disc = purchase_amount * discount
    total_withdisc = purchase_amount - amount_disc
    print("With the 20% discount, your total comes out to: $", total_withdisc)
elif purchase_amount >= 75:
    discount = .15
    amount_disc = purchase_amount * discount
    total_withdisc = purchase_amount - amount_disc
    print("With the 15% discount, your total comes out to: $", total_withdisc)
elif purchase_amount >= 50:
    discount = .10
    amount_disc = purchase_amount * discount
    total_withdisc = purchase_amount - amount_disc
    print("With the 10% discount, your total comes out to: $", total_withdisc)
elif purchase_amount >= 25:
    discount = .5
    amount_disc = purchase_amount * discount
    total_withdisc = purchase_amount - amount_disc
    print("With the 5% discount, your total comes out to: $", total_withdisc)
elif purchase_amount >= 0.01:
    print("Your total is: ", purchase_amount)
else:
    print("Error: You have entered a number lower than 1 cent.")