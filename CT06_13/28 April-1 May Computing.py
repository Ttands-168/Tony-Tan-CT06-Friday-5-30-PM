x = [20]
y = [23, 18]
print(x + [])
print(x + y)
print(y + x)
print(x * 3)
print(2 * y)
print(x + [65] + y)

result = []
result = ['First'] + result
result = ['Second'] + result
result = ['Third'] + result
print(result)

l = [2, 0, 2, 4]
result = l[0]
print(result)
result = l[-2]
print(result)
result = l[1:]
print(result)
result = l[1:-1]
print(result)
result = l[::2]
print(result)
result = l[::-1]
print(result)
result = l[::2][1]
print(result)
result = l[:999]
print(result)
result = l[:-999]
print(result)
result = l[:]
print(result)

del l[0]
del l[1]
del result
del l[::2]
del l[::-1]
del l[:999]
del l[:-999]
del l[:]

names_2023 = ['Beatrice', 'Celeste', 'DianaSer', 'Siewling', 'Jasmine', 'Sorling']
names_2023[0] = 'Alex'
print(names_2023)

x = ['a', 'b', 'c']
print(x[1])
x[1] = 'z'

names_2023 = names_2023[:2] + names_2023[3:]
print(names_2023)
names_2023.append(2, 'Beatrice') # This will raise an error because 2 ar
del names_2023[3]
print(names_2023)