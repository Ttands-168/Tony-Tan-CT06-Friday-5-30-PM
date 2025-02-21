import random
random_float = random.uniform(0, 38)

print("I have a hidden number from 0 to 38.")
print("Guess my hidden number.")

tries = 5

while tries > 0:
    user_input = float(input("What is your number? "))
    if user_input > 38 or user_input < 0:
        print("This is not a valid input.")
    else:
        if user_input > random_float + 0.25:
            print("This is too large - guess a smaller number.")
            tries = tries - 1
        elif user_input < random_float - 0.25:
            print("This is too small - guess a larger number.")
            tries = tries - 1
        else:
            print("Good job! You got the right answer! The float is " + str(random_float) + ".")
            break
if tries <= 0:
print("Game Over!")
print("The number is " + str(random_float) + ".")