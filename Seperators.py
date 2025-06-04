number = input("Please enter a series of numbers using different seperators")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)