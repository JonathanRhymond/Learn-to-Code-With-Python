def add_positive_numbers(a, b):
    try:
        if a<=0 or b <=0:
            raise ValueError(f"{a} or {b} is invalid. Make sure both numbers are greater than 0.")
        return a+b
    except ValueError as e:
        return (f"Caught the ValueError: {e}")

print(add_positive_numbers(10, 5))
print(add_positive_numbers(-2, 3))
print(add_positive_numbers(5, -8))