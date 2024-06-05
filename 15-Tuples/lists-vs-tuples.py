birthday = (7, 17, 2004)

print(len(birthday))

print(birthday[0])
# print(birthday[15])
print(birthday[-1])

# birthday[1] = 6 WONT WORK

addresses = (
    ["Hudson Street", "New York", "NY"],
    ["Franklin Street", "San Francisco", "CA"]
)

# addresses[1]  =["Something Else"] STILL WON'T WORK
addresses[1][0] = "Polk Street"
print(addresses)

print(dir(birthday))