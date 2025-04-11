word = input("Gimme a word. ")
found_e = False
found_o = False
while not(found_e and found_o and len(word) == 5):
    print("Got it! " + word + ".")
else:
    print("Not a good choice.")

counter = 60
while counter > 0:
    print(counter)
    counter -= 1