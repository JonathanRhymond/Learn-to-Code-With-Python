units = ["meter", "kilogram", "second", "ampere", "kelvin" ,"candela", "mole"]
more_units = units.copy()
units.remove("kelvin")
even_more_units = units[:]
units.remove("meter")

print(units)
print(more_units)
print(even_more_units)

