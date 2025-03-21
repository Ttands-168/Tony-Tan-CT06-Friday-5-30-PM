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

user_input1 = float(input("Give me the start number. "))
user_input2 = float(input("Give me the end number. "))
the_print = random.random() * 37
if user_input1 <= the_print <= user_input2:
    print(True)
else:
    print(False)
print(the_print)

num1 = random.random() * 50
num2 = random.random() * 50
question = float(input("What is " + str(num1) + " + " + str(num2) + "? "))
answer = num1 + num2
if answer - 0.4 <= question <= answer + 0.4:
    if answer - 0.25 <= question <= answer + 0.25:
        print("Really good huh!")
    else:
        print("Good effort")
else:
    print("Wrong. The answer is " + str(answer) + ".")