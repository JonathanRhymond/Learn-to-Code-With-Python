numbers = [3, 4, 5, 6, 7]

# squares = []
# for number in numbers:
#     squares.append(number ** 2)

squares = [number ** 2 for number in numbers]

print(squares)
print(numbers)

rivers = ["Amazon", "Nile", "Yangtze"]

print([len(river) for river in rivers])
print(rivers)

expressions = ["lol", "rofl", "lmao"]

print([expression.upper() for expression in expressions])
print(expressions)

decimals = [4.95, 3.28, 1.08]

print([int(decimal) for decimal in decimals])
print(decimals)
