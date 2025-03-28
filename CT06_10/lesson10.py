number = float(input("What is the number? "))
if number % 2 == 0:
    print("It is an even number.")
elif number % 2 == 1:
    print("It is an odd number.")
else:
    print("It is a decimal.")

age = float(input("How old are you? "))
if age < 12.5:
    print("You are a child.")
elif age < 21:
    print("You are an adolescent.")
elif age < 65:
    print("")