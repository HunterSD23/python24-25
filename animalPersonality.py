print(List of Animals: Dog, Cat, Lion, Tiger, Rabbit, Bird, Dolphin, Elephant, Sloth, Turtle)
fav_animal = input("Pick which animal is your favorite: ").lower.str

if fav_animal == "dog" or "cat":
    print("You are very family oriented! You like to relax a lot, but you wouldn't mind spending time with friends.")
elif fav_animal == "lion" or "tiger":
    print("You are brave and unfazed to most things. You have incredible focus when it comes to certain things. You also tend to relax when you can.")
elif fav_animal == "rabbit" or "bird":
    print("You are constantly in fear.")
elif fav_animal == "dolphin" or "turtle":
    print("You like the sea, and you probably have a lot of fish in your house.")
elif fav_animal == "elephant" or "sloth":
    print("You are veryyy relaxed, but you can fight if you have to.")
else:
    print("Error: That wasn't an animal on the list.")