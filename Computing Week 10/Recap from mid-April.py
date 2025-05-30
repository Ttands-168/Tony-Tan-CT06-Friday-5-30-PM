import time
import math
# Celeste and celeste are case-sensitive
# Use underscores instead of hyphens in variable names
box_size = 80 # not size_correct?
print("Box size is", box_size)
# You are discouraged from using break and continue in loops
count = 10
while count > 0:
    print("Count is", count)
    count -= 1
    time.sleep(1)  # Sleep for 1 second to simulate a delay
print("Countdown finished!")
# Use meaningful variable names instead of generic ones
# Don't use exclamation marks unless NOT in a string

x = 5
y = 3

(x + y) ** 2 == x**2 + 2*x*y + y**2 # This is an example of how you perform a function
# Use Celeste2024 instead of 2024Celeste as a variable name
# Don't use country names as variable names unless they are relevant to the context
India = 1,440,000,000  # Population of India
China = 1,410,000,000  # Population of China
United_States = 340,000,000  # Population of the United States 2025
theta = x  # Use descriptive names for angles

class_1940 = False # Because Germany was depressed in 1940
Germany = 79,000,000  # Population of Germany in 1940

del count # Some variables may cause confusion later
name = input("What is your name? ") # Ask for the user's name
print("Hello, " + name + "!")  # Greet the user
# Use spacing inside an input string
poem = input("What is inside your poem? ") # Curious about the user's poem
print("Your poem is:", poem)  # Display the user's poem
print("Oh, fish in the sea, so wild and free, I am Celeste, please listen to me!") # So beautiful a poem!

del poem

sodium_hydroxide = "NaOH"  # Chemical formula for sodium hydroxide
sodium_methoxide = "NaOCH3"  # Chemical formula for sodium methoxide
sodium_ethoxide = "NaOC2H5"  # Chemical formula for sodium ethoxide
sodium_ozonide = "NaO3"  # Chemical formula for sodium ozonide
hydrogen_sulfate = "H2SO4"  # Chemical formula for hydrogen sulfate
print("The aqueous form of hydrogen sulfate is sulfuric acid:", hydrogen_sulfate)  # Display the chemical formula for hydrogen sulfate
print("The pH of sodium methoxide is about 12-14, making it a strong base.")  # Display the pH of sodium methoxide
methanol = "CH3OH"  # Chemical formula for methanol
print("Methanol has a pH of about 7, making it neutral:", methanol)  # Display the pH of methanol
print("Sodium hydroxide is a strong base with a pH of about 14:", sodium_hydroxide)  # Display the pH of sodium hydroxide

bone_age = float(input("What is your bone age? "))  # Ask for the user's bone age
current_height = float(input("What is your current height in metres? "))  # Ask for the user's current height in meters
if bone_age < 0 or current_height < 0:
    print("Bone age and height must be positive numbers.")  # Check for valid input
elif bone_age <= 1:
    print("You will grow by 20cm from now until you are 1 year old.")  # If bone age is less than or equal to 1, the user will grow by 20 cm
elif bone_age <= 11:
    print("You will grow by about 5-10 cm in the next year.") # Pre-puberty growth
elif bone_age <= 14:
    print("You are growing bigger and taller!")  # If bone age is less than or equal to 14, the user is growing
elif bone_age <= 16:
    print("You will grow by about 3-5 cm in the next year.")  # If bone age is less than or equal to 16, the user will grow by 3-5 cm
else:
    print("You can't grow much taller now.")  # If bone age is greater than 16, the user can't grow much taller
# Use descriptive variable names for bone age and height
if current_height < 1.55 and bone_age > 16:
    print("You are short for your age.")  # If current height is less than 1.55 meters and bone age is greater than 16, the user is short for their age
elif current_height < 1.65 and bone_age > 16:
    print("You are average height for your age.")
elif current_height < 1.65 and bone_age <= 15:
    print("You are still growing taller!")  # If current height is less than 1.65 meters and bone age is less than or equal to 15, the user is still growing taller
elif current_height < 1.75 and bone_age <= 14:
    print("You are growing taller!")
elif current_height < 1.85 and bone_age <= 13:
    print("Wow, you are on track to be 2+ metres tall!")  # If current height is less than 1.85 meters and bone age is less than or equal to 13, the user is on track to be 2+ meters tall
elif current_height > 1.7 and bone_age > 16:
    print("You are tall for your age.")
elif current_height > 1.8 and bone_age > 16:
    print("You are very tall for your age.")