breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

# print(zip(breakfasts, lunches, dinners))
# print(type(zip(breakfasts, lunches, dinners)))
# print(list(zip(breakfasts, lunches, dinners)))

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meals for today were {breakfast}, then {lunch}, and finally {dinner}")