pizzas = [
    "Mushroom",
    "Pepperoni",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))
if "Olives" in pizzas: # check for value before calling index to avoid error
    print(pizzas.index("Olives"))
print(pizzas.index("Pepperoni", 2)) # start search from index 2
print(pizzas.index("Sausage", 3))
print(pizzas.index("Sausage", 2)) # search is inclusive