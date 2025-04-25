print('Hello World'.endswith('ld'))
print('2025'.startswith('20'))
print('CS2025'.find('20'))
print('CS2025'.find('21'))
print('A AA AAA'.split())
print('A AA AAA'.split(' '))
print('Index,5, 88,3!'.split(','))
print('PIZza'.lower())
a = 'Hello'
print(a.upper())
print('PIZza'.islower())
print('CS2025'.isupper())
print('   '.isspace())
print('  Computing'.isspace())
print('Computing2025'.isalnum())
print('Computing 2025'.isalnum())
print('computing'.isalpha())
print('CS2025'.isalpha())
print('2025'.isdigit())
print('2025   '.isdigit())

x = 'Hello'
y = "World"
print('Hello' + "World")
print(x + y)
print(x * 2)
print(2 * x)
print(x + " " + y)

p = "ba"
q = "na"
print(p + q * 2)
print("man" in "maneater")
print("eat" not in "theatre")
print(len("maneater"))

s = "Computing"
s[0]
s[3]
s[-2]
s[0:2]
s[1:2]
s[:2]
s[::2]
s[0::4]
s[9:0:-2]

del s
Computing = "Gothic"
City_Hall = "City Hall MRT Station"
print(Computing + " " + City_Hall + " is not in Singapore. However, there is a City Hall MRT Station in Singapore.")

del Computing
del City_Hall
print("A Computing hub is located in City Hall MRT Station.\n And City Hall MRT Station is really crowded.")
print("A Computing hub is located in City Hall MRT Station.\t And City Hall MRT Station is really crowded.")

first = "First, preheat the oven to 180 deg. C.\nThen, rub in the flour with the butter using your fingertips until it resembles breadcrumbs.\nThen, make a well in the centre and add cold water.\n"
second = "Next, roll and shape the dough and cut the dough using a biscuit cutter.\nAfter that, coat the top of the dough with egg wash.\nFinally, bake in the oven for 10-15 minutes until golden brown and leave it to cool for 5 minutes.\nEnjoy your scones!"
print(first + second)
del first
del second
print('2024 is Bala\'s first year of studying Computing.')

x = "There are {} types of people in this world.".format(0b10)
type1 = "cannot"
type2 = "binary"
y = "Those who read {1} and those who {0}.".format(type1, type2)
print(x)
print(y)

del type1
del type2
del x
del y
start = "Hello, "
name = input("What is your name? ")
end = "\n Welcome to my therapy session."
sentence = start + name + end
print(sentence)
del start
del name
del end
del sentence

movie = input("What is your favourite movie? ")
age = input("How old are you? ")
print("At age {}, your favourite movie is {}.".format(age, movie))
del movie
del age

height = input("What is your height in cm? ")
mass = input("What is your mass in kg? ")
BMI = float(mass) / ((float(height) / 100) ** 2)
print("Your BMI is {}.".format(BMI))