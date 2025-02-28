# score_one = 80
# score_two = 90
# score_three = 75
# total = score_one + score_two + score_three
# average_score = total / 3
# student_name = "Alex"
# print("Average score for " + student_name + " is: " + str(average_score))

# for ubi_ave_1 in range(1, 11):
#     print(ubi_ave_1)
# for ubi_ave_2 in range(2, 21, 2):
#     print(ubi_ave_2)
# for ubi_ave_3 in range(10, 0, -1):
#     print(ubi_ave_3)

word = input("What string do you want me to repeat? ")
repeating = int(input("How many times do you need me to repeat this word. "))

for count in range(repeating):
    print(word)

name_rot = input("What is your name? ")
message = input("What message do you want me to send to you? ")
n = int(input("How many times do you want me to repeat? "))

for k in range(n):
    print(message + name_rot)

