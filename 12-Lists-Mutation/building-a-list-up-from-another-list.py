powerball_numbers = [4, 8, 15, 16, 23, 42]
print(powerball_numbers)

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number **  2)
    return squares
print(squares(powerball_numbers))

def convert_to_floats(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats
print(convert_to_floats(powerball_numbers))
print(convert_to_floats(squares(powerball_numbers)))

def even_or_odd(numbers):
    results =[]
    for number in numbers:
        results.append(number%2==0)
    return results
print(even_or_odd(powerball_numbers))