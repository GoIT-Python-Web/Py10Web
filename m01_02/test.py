data = [1, 2, 3, 4]

one = data[0]
print(one)

one, two, *rest = data

print(*rest)
print(one)
