import random
while True:
    word = input("Gimme a word. ")
    found_e = word.find('e')
    found_o = word.find('o')
    if not(found_e and found_o and len(word) == 5):
        print("Not a good choice.")
    else:
        print("Got it! " + word + ".")
        break


counter = 60
while counter > 0:
    print(counter)
    counter -= 1

while True:
    visitors_already_present = int(input("How many visitors are there? "))
    if visitors_already_present < 50:
        print("You can add more.")
        break
    else:
        print("Sorry, we are full!")
        break

del visitors_already_present
order = ""
while True:
    order2 = input("What is your order? ")

del order
count_time = 0
score = 0
while True:
    counter += 1
    number1 = random.random() * 37
    number2 = random.random() * 37
    operator = random.randint(1, 4)

    if operator == 1:
        question = "Find the value of " + str(num1) + " + " + str(num2) + ": "
        answer = float(input(question))
        hidden_answer = number1 + number2
    elif operator == 2:
        question = "Find the value of " + str(num1) + " - " + str(num2) + ": "
        answer = float(input(question))
        hidden_answer = number1 - number2
    elif operater == 3:
        question = "Find the value of " + str(num1) + " x " + str(num2) 
    if hidden_answer - 0.25 <= answer <= hidden_answer + 0.25:
        print("Correct!")
        break
    else:
        print("Wrong! Try again!")