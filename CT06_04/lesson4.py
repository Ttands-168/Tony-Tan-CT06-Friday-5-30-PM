orange_plate = 1.2
yellow_plate = 2.2
green_plate = 3
cyan_plate = 4.5
real_turquoise_plate = 6

customer1 = orange_plate * 3 + yellow_plate * 5 + green_plate * 4
customer2 = yellow_plate * 2 + cyan_plate * 5
customer3 = orange_plate * 20 + cyan_plate
print("Noor Daanya is paying $" + str(customer1) + " to Mr Hong Guozhong for this.")
print("Khoo Siew Ling is paying $" + str(customer2) + " to Mr Huang Jonkin for this.")
print("Smahon Loh is paying $" + str(customer3) + " to Ms Celeste Loh for this.")

Smahon_Loh_money = float(input("Mrs Smahon, how much do you have in your wallet?"))
Smahon_Loh_money_1_hour_later = Smahon_Loh_money - customer3
Smahon_Loh_money_1_year_later = Smahon_Loh_money_1_hour_later * 1.0425
print("You will have $" + str(Smahon_Loh_money_1_year_later) + " next year.")

Name1 = input("What is your name? ")
Colour1 = input("Which colour resonates with your personality? ")
Age1 = input("How old are you? ")
print("Hello " + Name1 + "! You are " + Age1 + " years old and your colour is " + Colour1 + ".")

Name2 = input("What is your name? ")
Hobby2 = input("What do you like doing in your free time? ")
Dream_Vacation2 = input("If you have a 1 year paid leave, where do you want to go? ")
print("Hello " + Name2 + "! I also like " + Hobby2 + " and I actually want to go to " + Dream_Vacation2 + " too!")

Age3 = float(input("How old are you currently? "))
Age2 = Age3 + 50
Age2 = ("You will be " + Age2 + " years old in 2075.")
Number = float(input("Your number is? "))
Number2 = Number * 2
print("The enemy will attack " + Number2 + " and 43 at 6:20 PM on February 15, 2025. Be prepared.")
