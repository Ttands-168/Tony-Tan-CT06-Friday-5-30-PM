found_e = False
found_o = False
while True:
    word = input("Gimme a word. ")
    while not(found_e and found_o and len(word) == 5):
        print("Not a good choice.")
    else:
        print("Got it! " + word + ".")


counter = 60
while counter > 0:
    print(counter)
    counter -= 1

visitors_already_present = input("")