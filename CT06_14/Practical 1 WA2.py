import time
# let x be 10
x = 10
while x <= 200:
    print(x)
    x += 10
    time.sleep(1)

# Don't get hacked
password = "superpass123"
granted = False
while granted == False:
    user_input = input("Enter the password. ")
    if user_input == password:
        granted = True
        print("Access granted")
    else:
        print("Access denied")
        continue