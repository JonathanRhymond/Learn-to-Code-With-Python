capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
}
print(capitals)

inverted = {capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(inverted)