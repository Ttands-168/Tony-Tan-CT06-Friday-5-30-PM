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
students = ["Aidan", "Alex", "Belinda", "Bernice", "Celeste Tan", "Celeste Kim", "Diana", "Ethan Tian", "Ethan Wong", "Felicia", "Glenda", "Kayson", "Koko", "Lisa", "Lucas", "Nancy", "Paulina", "Quincy", "Ravi", "Ryan", "Tony", "Vincent"]
groceries = ["Banana", "Bacon", "Chicken" "Corn", "Dark Chocolate", "Eggs", "Falfel"]