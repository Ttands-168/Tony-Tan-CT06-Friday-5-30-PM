x = 456
x += 155
print(x)
x -= 488
x -= 87
print(x)
x = 256
x /= 8
print(x)
x += 15
x *= 13
print(x)
x -= 548
x /= 21
x += 6
print(x)

del x

n = 47//5
print(n)
n += 15
n %= 5
print(n)
n /= 2
n **= 4
print(n)

del n

a = 15
b = 7
c = 5
d = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(c // d)
print(c % d)
print(c ** d)

del c
del d

a = 5
b = 6.0
print(a + b)

a = 9
b = 3
a -= b
print(a)

a = 9
b = 3
a /= b
print(a)

a = 3
b = 4
a **= b
print(a)

a = 4
b = 3
a %= b
print(a)

del a
del b

base = float(input("What is the base of the triangle? "))
height = float(input("What is the height of the triangle? "))
area = 0.5 * base * height
print("The area of the triangle is " + str(area) + " square units.")
# The area of a triangle is given by the formula: area = 0.5 * base * height

del base
del height
del area

