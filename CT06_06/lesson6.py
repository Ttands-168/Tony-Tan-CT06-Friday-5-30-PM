# For loop lesson 5
num1 = input("Give me your start value. ")
num2 = input("Give me your end value. ")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    for Russia in range(num2, num1):
        print(Russia)
else:
    for Russia in range(num1, num2):
        print(Russia)