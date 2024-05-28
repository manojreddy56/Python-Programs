number = "9,223;372:036 854,775;805"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else" "for char in number).split()
print([int(val) for val in values])