import random
word = input("Gimme a word. ")
found_e = word.find('e')
found_o = word.find('o')
while not(found_e and found_o):
    print("Not a good choice.")
else:
    print("Got it! " + word + ".")


counter = 60
while counter > 0:
    print(counter)
    counter -= 1

while True:
    visitors_already_present = int(input("How many visitors are there? "))
    while visitors_already_present < 50:
        print("You can add more.")
    else:
        print("Sorry, we are full!")

del visitors_already_present
order = ""
while True:
    order2 = input("What is your order? ")

del order
number1 = random.random() * 37
number2 = random.random() * 37
question = float(input("Find the value of " + str(num1) + " + "))