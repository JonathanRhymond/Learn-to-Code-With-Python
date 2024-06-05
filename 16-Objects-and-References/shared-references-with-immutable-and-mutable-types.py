a = 3
b = a # pointing to different objects
a = 5
print(a)
print(b)

a = [1, 2, 3]
b = a # pointing to the same object
a.append(4)
print(a)
print(b)