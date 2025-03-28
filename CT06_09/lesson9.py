import time
import math
import random
# Sleep_Time = int(input("How many seconds do you want me to count down? "))
# for i in range(60, 0, -1):
#     time.sleep(1)
#     print(i)
# print("Happy New Year!")
# print(random.randint(3, 18))
# for i in range(20):
#     time.sleep
#     print(random.randint(0, 9999))

# num1 = random.random() * 37
# num2 = random.random() * 20
# print(num1)
# print(num2)
# integer = float(input("What is the sum of the two numbers? "))
# if integer + 0.25 >= num1 + num2 and integer - 0.25 <= num1 + num2:
#     print("good job!")
# else:
#     print("Oops, you are wrong!")

# # user_input1 = float(input("Give me the start number. "))
# # user_input2 = float(input("Give me the end number. "))
# # the_print = random.random() * 37
# # if user_input1 <= the_print <= user_input2:
# #     print(True)
# # else:
# #     print(False)
# # print(the_print)

# num1 = random.random() * 50
# num2 = random.random() * 50
# question = float(input("What is " + str(num1) + " + " + str(num2) + "? "))
# answer = num1 + num2
# if answer - 0.4 <= question <= answer + 0.4:
#     if answer - 0.25 <= question <= answer + 0.25:
#         print("Really good huh!")
#     else:
#         print("Good effort")
# else:
#     print("Wrong. The answer is " + str(answer) + "

# user_input_9 = float(input("What is your number? "))
# remainder = user_input_9 % 2
# if remainder == 0:
#     print("It is an even number.")
# elif remainder == 1:
#     print("It is an odd number.")
# else:
#     print("It is a decimal.")

# user_input_10 = float(input("Give me a number. "))
# user_input_11 = float(input("Give me a second number. "))
# if user_input_10 % user_input_11 == 0:
#     print("You can divide your 1st input by your second input.")
# else:
#     print("You cannot divide. Waaaaa!")

# user_input = int(input("What is the random number? "))
# real_magic_number = random.randint(1, 10)
# print( user_input == real_magic_number )

oranges = float(input("How many oranges are there? "))
apples = float(input("How many apples you have? "))

price_of_apples = apples * 0.45
price_of_oranges = oranges * 0.60

if apples > 5:
    price_of_apples = price_of_apples * 0.9

if oranges > 5:
    if oranges > 10:
        price_of_oranges = price_of_oranges * 0.75
    else:
        price_of_oranges = price_of_oranges * 0.9

print("The prices of your groceries is $" + str(price_of_apples + price_of_oranges) + ".")