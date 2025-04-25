# Lesson 12 recap
while True:
    user_balance = 10
    options = input("Enter the options. ")
    if options == "deposit":
        deposit = float(input("How much money do you want to deposit?"))
        user_balance += deposit
    if options == "withdraw":
        withdraw = float(input("How much money do you want to withdraw?"))
        user_balance -= withdraw
    if options == "loan":
        loan = float(input("How much loan do you want to take out?"))
        user_balance -= loan
        