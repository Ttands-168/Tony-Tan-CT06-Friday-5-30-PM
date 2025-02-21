import random
random_float = random.uniform(0, 38)

print("I have a hidden number from 0 to 38.")
print("Guess my hidden number.")

tries = 5

while tries > 0:
    user_input("What is your number?")