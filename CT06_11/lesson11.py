number = float(input("What number are you looking at? "))
if number % 3 == 0 and number % 7 == 0:
    print("The number is divisible by both 3 and 7.")
else:
    print("The remainder is " + str(number % 21) + ".")

height = float(input("What is your current height in centimetres? "))
if height < 100:
    print("You can't ride!")
elif height < 120:
    print("You can ride with supervision.")
else:
    print("You can ride yourself.")

Erik_Heng = 17
Tony_Tan = 15

if Erik_Heng >= 18 or Tony_Tan >= 18:
    print("You can ride on a go-kart.")
else:
    print("Someone older than you must manage because Erik is not 18 yet.")

age = float(input("How old are you? "))

if age < 13 or age > 64:
    print("Ticket costs $12.")
else:
    print("Ticket is $800.")

del age

cyan = input("What is the colour? ")
while cyan != "cyan" or cyan != "Cyan":
    print("It is not " + cyan + ".")
else:
    print("Ok, SSundee")