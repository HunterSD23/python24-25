prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

# while message != 'quit':
#     message = input(prompt)
#     print(message)


print("\n\nWhile Loop Using a Flag")
print("-----------------------")

active = True # Programming Flag

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)