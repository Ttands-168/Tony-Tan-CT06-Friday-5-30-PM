word = input("Gimme a word. ")
found_e = False
found_o = False
if found_e and found_o and len(word) == 5:
    print("Got it! " + word + ".")
    continue
else:
    print("Not a good choice.")

counter = 60
while counter > 0:
    print(counter)
    counter -= 1