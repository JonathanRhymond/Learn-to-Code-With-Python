foods = "Sushi", "Steak", "Guacamole"
foods = ("Sushi", "Steak", "Guacamole") # best practice, NOT required

print(type(foods))

empty = ()
print(type(empty))

# mystery = (1)
# print(type(mystery))

mystery = (1,)
print(type(mystery))

print(tuple(["Steak", "Steak", "Guacamole"]))
print(type(tuple(["Steak", "Steak", "Guacamole"])))

print(tuple(["abc"]))
print(type(tuple(["abc"])))