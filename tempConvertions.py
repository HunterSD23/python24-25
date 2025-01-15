def celsius_to_fahrenheit(celsius):
    """_summary_

    Args:
        celsius (float): temperature in Celsius

    Return:
        float: temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """_summary_

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Return:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

# Ask the user what convertion they need to do.
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

# Process the users choice
if choice == "1":
    celsius = float(input("Enter temperature in celsius: "))
    print(f"{celsius}*C is equal to {celsius_to_fahrenheit(celsius):.2f}")
elif choice == "2":
    fahrenheit = float
else:
    print("Invalid choice!")