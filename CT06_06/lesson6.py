# For loop lesson 5
num1 = input("Give me your start value. ")
num2 = input("Give me your end value. ")

num1 = float(num1)
num2 = float(num2)

if num1 > num2:
    for Russia in range(float(num2), float(num1)):
        print(Russia)
else:
    for Russia in range(float(num1), float(num2)):
        print(Russia)