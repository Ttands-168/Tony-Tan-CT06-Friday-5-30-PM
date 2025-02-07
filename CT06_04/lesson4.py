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

Smahon_Loh_money = int(input("Mrs Smahon, how much do you have in your wallet?"))
Smahon_Loh_money_1_hour_later = Smahon_Loh_money - customer3
Smahon_Loh_money