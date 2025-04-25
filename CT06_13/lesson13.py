# Lesson 12 recap
user_balance = 10
while True:
    options = input("Enter the options. ")
    if options == "deposit":
        deposit = float(input("How much money do you want to deposit? "))
        user_balance += deposit
    if options == "withdraw":
        withdraw = float(input("How much money do you want to withdraw? "))
        user_balance -= withdraw
        if user_balance < 0:
            print("You owe the bank $" + str(-user_balance) + ". If you do not pay by 7 days, you will get charged 2\")
    if options == "loan":
        loan = float(input("How much loan do you want to take out? "))
        user_balance -= loan
    if options == "check balance":
        print("You currently have $" + str(user_balance) + " in your account.")
    if options == "exit":
        print("Thank you for using the bank.")
        break