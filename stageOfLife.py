print("\n###############################################")
print("###                                         ###")
print("###         Stage of Life Program           ###")
print("###                                         ###")
print("###############################################\n\n")


user_name = input("Please Enter Your Name: ")
user_age = int(input("Please Enter Your Age: "))

print("\n###############################################")
print("###                                         ###")
print("###                  Results                ###")
print("###                                         ###")
print("###############################################\n\n")

print("\nHello", user_name)
if user_age <= 100 and user_age >= 66:
    print("You are currently in the Retirement stage of your life. \n")
elif user_age <= 65 and user_age >= 56:
    print("You are currently in the Wise Person stage of your life. \n")
elif user_age <= 55 and user_age >= 30:
    print("You are currently in the Adult stage of your life. \n")
elif user_age <= 29 and user_age >= 20:
    print("You are currently in the Young Adult stage of your life. \n")
elif user_age <= 19 and user_age >= 13:
    print("You are currently in the Teenager stage of your life. \n")
elif user_age <= 12 and user_age >= 8:
    print("You are currently in the childhood stage of your life. \n")
else: 
    print("Sorry, but you're too young or old to be registered with an age group. \n")