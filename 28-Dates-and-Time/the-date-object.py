# import datetime
from datetime import date

birthday = date(2004, 7, 17)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

# date(2025, 15, 10)
# date(2021, 2, 29) # would not throw error in leap year

print(birthday.year)
print(birthday.month)
print(birthday.day)

# birthday.year = 2000

today = date.today()
print(today)
print(type(today))

print(today-birthday)