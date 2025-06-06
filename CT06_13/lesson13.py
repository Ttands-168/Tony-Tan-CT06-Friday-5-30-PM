# Lesson 12 recap
user_balance = 10
while True:
    options = input("Enter the options. ")
    if options == "deposit":
        deposit = float(input("How much money do you want to deposit? "))
        user_balance += deposit
    elif options == "withdraw":
        withdraw = float(input("How much money do you want to withdraw? "))
        user_balance -= withdraw
        if user_balance < 0:
            print("You owe the bank $" + str(-user_balance) + ". If you do not pay by 7 days, you will get charged 21% compound interest daily.")
    elif options == "loan":
        loan = float(input("How much loan do you want to take out? "))
        user_balance -= loan
        print("You are charged 5% compound interest a year.")
    elif options == "check balance":
        print("You currently have $" + str(user_balance) + " in your account.")
    elif options == "exit":
        print("Thank you for using the bank.")
        break
    else:
        print("Sorry, I do not understand that option.")

# Start of Lesson 13
import time

students = ["Aidan", "Alex", "Belinda", "Bernice", "Celeste Tan", "Celeste Kim", "Diana", "Ethan Tian", "Ethan Wong", "Felicia", "Glenda", "Kayson", "Koko", "Lisa", "Lucas", "Nancy", "Paulina", "Quincy", "Ravi", "Ryan", "Tony", "Vincent"]
groceries = ["Banana", "Bacon", "Beef", "Chicken", "Cornflakes", "Dark Chocolate", "Eggs", "Falfel", "Floor Cleaners", "Honey", "Kale", "Kaya", "Lettuce", "Mac N Cheese", "Peanut Butter"]
print(groceries)
groceries.insert(3, "Bread")
print(groceries)
del groceries[5]
print(groceries)

for buying in groceries:
    time.sleep(1)
    if buying == "Bacon":
        print("Buy the less fatty bacon.")
    elif buying == "Chicken":
        print("I need 2 packets of chicken.")
    elif buying == "Eggs":
        print("I need 20 eggs.")
    elif buying == "Peanut Butter":
        print("Buy the Skippy.")
    else:
        print("I need 1 " + buying + ".")

groceries = []
while True:
    user_input = input("What items have you added to the basket? ")
    if user_input.lower() == "no more" or user_input.lower() == "end":
        print("Thank you for shopping!")
        break
    groceries.append(user_input)
    print(groceries)

# Print the 14 times table
number = 14
while number <= 168:
    print(number)
    number += 14
    time.sleep(1)
else:
    print("End")

catalogue = ["Celeste", "Diana", "Ethan Tian", "Kamala", "Terence", "Othman Tian", "Kim"]
found = False
dating = input("Who do you want to date? ")
for person in catalogue:
    if dating.lower() == person.lower():
        print("Yes, I found " + person + ". " + person + " is all yours now.")
        found = True
        catalogue.pop(str(dating))
        break
    if not found:
        print("Sorry, we don't have " + dating + ". Sorry.")