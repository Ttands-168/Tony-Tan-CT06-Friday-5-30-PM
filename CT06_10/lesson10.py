number = float(input("What is the number? "))
if number % 2 == 0:
    print("It is an even number.")
elif number % 2 == 1:
    print("It is an odd number.")
else:
    print("It is a decimal.")

age = float(input("How old are you? "))
if age < 12.5:
    print("You are a child.")
elif age < 21:
    print("You are an adolescent.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an old man.")

temperature = float(input("What is the temperature outside today? "))
if temperature < 4:
    print("You can go skiing.")
elif temperature < 10:
    print("Please go bowling.")
elif temperature < 16:
    print("You can play computer games or read or do your homework or something.")
elif temperature < 31:
    print("It's time to go outside and play.")
else:
    print("It is blazing hot you can go swimming.")

score = float(input("Tell me your score. "))
if 75 <= score <= 100:
    print("Yay! You got A1!")
elif 70 <= score <= 75:
    print("Well, A2, some room for improvement, not too bad.")
elif 65 <= score <= 70:
    print("You scored B3. Keep improving!")
elif 60 <= score <= 65:
    print("Hmm, B4, not too bad, but keep working hard.")
elif 55 <= score <= 60:
    print("You need to work harder. You scored C5.")
elif 50 <= score <= 55:
    print("You scored C6 - horrible but still a pass.")
elif 45 <= score <= 50:
    print("You failed with a D7! You stupid or what?")
elif 40 <= score <= 45:
    print("Why the hell you scored E8!")
elif 0 <= 40:
    print("Why the fuck you got F9!")
elif score < 0:
    print("Huh? What is this? G10?")
else:
    print("Wah! So good? Better than A1?")

age2 = float(input("How old are you? "))
if age < 0:
    print("You are not born yet.")
elif age < 21:
    print("You are not allowed to vote.")
elif age < 140:
    print("You are eligible to vote this round.")
else:
    print("You would have already died.")

price = float(input("What is the price of something you want to buy? "))
if price < 25:
    safety = input("Sounds good. Is the item safe to use? ")
    if safety == "Yes" or safety == "yes":
        print("Ok. Buy it!")
    else:
        print("No!")
elif price < 250:
    credibility = input("Are you sure you want it? ")
    if credibility == "Yes" or credibility == "yes":
        print("Ok, buy it! I am not responsible for your loss.")
elif price < 750:
    credibility2 = input("Where did you get this money from? ")
    if credibility2 == "My piggy bank" or credibility2 == "My wallet" or credibility2 == "My savings":
        print("Yes, but don't get me responsible if you lose the valuable item.")
    elif credibility2 == "stealing" or credibility2 == "by stealing" or credibility2 == "By stealing":
        print("No! Give back the money or I will call the police!")
    else:
        print("No! You can't buy it!")
else:
    print("Don't even think of buying it!")