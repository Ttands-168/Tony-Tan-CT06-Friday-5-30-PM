# Lesson 12 recap
user_balance = 10
while True:
    options = input("Enter the options. ")
    if options == "deposit":
        deposit = float(input("How much money do you want to deposit?"))
        user_balance += deposit
    if options == "withdraw":
        withdraw = float(input("How much money do you want to withdraw?"))
        user_balance -= 