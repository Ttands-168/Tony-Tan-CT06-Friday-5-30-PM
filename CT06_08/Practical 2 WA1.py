# Get the start value
a = int(input("Find the value of a."))
# Get the stop value
b = int(input("Find the value of b."))
# Get the increment value
c = int(input("Find the value of c."))
# For looping START!
if c < 0:
    if a > b:
        for i in range(a, b, c):
            print(str(i))