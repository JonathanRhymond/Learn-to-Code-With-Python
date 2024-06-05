# with open("cupcakes.txt", "r") as cupcakes_file: # r is default so not needed
#     print("The file has been opened")
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed. We are outside the context block!")

filename = input("What file would you like to open? ")
with open(filename, "r") as file_object:
    print(file_object.read())