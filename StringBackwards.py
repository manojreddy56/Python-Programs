letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

print()

    #create a slice that produces the characters qpo 
print(backwards[9:12])
print(letters[16:13:-1])
    #slice the string to produce edcba
print()

print(backwards[21:])
print(letters[4::-1])

print()
    #slice the string to produce the last 8 characters, in reverse order
print(backwards[:8])
print(letters[25:17:-1])