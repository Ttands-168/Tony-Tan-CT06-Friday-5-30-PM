found_e = False
found_o = False
word = input("Gimme a word. ")
for letter in word:
    while not(found_e and found_o):
        print("Not a good choice.")
    else:
        print("Got it! " + word + ".")


counter = 60
while counter > 0:
    print(counter)
    counter -= 1

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
math = True
