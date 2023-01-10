print("Welcome to the Solar System Quiz!")

playing = input("Would you like to play? (y/n) ")

if playing != "y":
    quit()

print("Let the quiz begin!")
score = 0

sun_answer = input("What is at the center of our solar system? ").lower()
if sun_answer == "sun":
    print("Correct!")
    score += 1
elif sun_answer == "the sun":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

earth_answer = input("What is the third planet from the sun? ").lower()
if earth_answer == "earth":
    print("Correct!")
    score += 1
elif earth_answer == "the earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

neptune_answer = input("What is the farthest planet from the sun? ").lower()
if neptune_answer == "neptune":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

mercury_answer = input("What is the closest planet to the sun? ").lower()
if mercury_answer == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

number_of_planets_answer = input("How many planets exist in our Solar System? ").lower()
if number_of_planets_answer == "8":
    print("Correct!")
    score += 1
elif number_of_planets_answer == "eight":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

jupiter_answer = input("What is the largest planet in our Solar System? ").lower()
if jupiter_answer == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

orbit_answer = input("What is the movement of planets around the sun called?(orbit/rotation) ").lower()
if orbit_answer == "orbit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print("You got " + str(score) + " out of 7.")
print(str(((score)/7) * 100) + "%")