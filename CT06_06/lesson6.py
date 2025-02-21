# For loop lesson 5
# num1 = input("Give me your start value. ")
# num2 = input("Give me your end value. ")

# num1 = int(num1)
# num2 = int(num2)

# if num1 > num2:
#     for Russia in range(num2, num1):
#         print(Russia)
# else:
#     for Russia in range(num1, num2):
#         print(Russia)

# Geography Test

Geography_Sec3 = int(input("How many students are in your class? "))
total_test_grade = 0
for students in range(1, Geography_Sec3 + 1):
    username = input("What is your name? ")
    individual_test_grade = float(input("What is your score for geography? "))
    total_test_grade = total_test_grade + individual_test_grade
average_test_grade = total_test_grade / Geography_Sec3
print("The average score for 3E Geography Test is " + str(average_test_grade) + ".")

# Debugging

# for i in range(3):
#     print("Hello, World!")

# for i in range(5):
#     print(i)

# print("Hello, World!")

# x = 5
# if x == 5:
#     print("They are 5!")

# print ("Hello, World!")

## Task 2: Name Errors

# age = 14.5
# print(age)


# name = "Alice"
# print(name)

# x = 5
# print(x)

age = 25
print(age + 1)


number = 10
print(number - 5)

repeat_num = 3
print("Repeat" * str(repeat_num))


year = 2023
print("The year is " + str(year))


x = 10
y = x / 2


end = "5"
for i in range(end):
    print(i)
