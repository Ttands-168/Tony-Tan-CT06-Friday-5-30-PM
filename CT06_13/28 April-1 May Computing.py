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