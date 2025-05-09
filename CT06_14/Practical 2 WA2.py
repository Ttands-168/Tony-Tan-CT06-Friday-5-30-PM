# Lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"]
print(planets[2])
# Append
planets.append("Neptune")
print(planets)
# Elon Musk conquered Mars
planets[3] = "Muskworld"
print(planets)
# Uranus no longer became a planet
planets.pop(6)
# For loops
a = 0
for a in planets:
    print(planets)
    a += 1