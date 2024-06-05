class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! The object is {self}.")

acoustic = Guitar()
print(acoustic)

electric = Guitar()
print(electric)

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

# print(wood)
# print(string)

print(acoustic.wood)
print(electric.nickname)

# print(electric.year)
# print(acoustic.nickname)