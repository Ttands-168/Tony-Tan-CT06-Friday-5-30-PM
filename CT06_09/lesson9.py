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

integer = int(input("What is the sum of the two numbers? "))
num1 = random.random() * 37
num2 = random.random() * 20
print(num1)
print(num2)
if integer + 0.25 >= num1 + num2 and integer - 0.25 <= num1 + num2:
    print("good job!")
else:
    print("Oops, you are wrong!")