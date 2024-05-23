import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Enter a valid number ")


answer = random.randint(1,10)
print(answer)

print("Please guess a number between 1 to 10: ")

while True:
    guess = get_integer(": ")
    if guess == answer:
        print("Well done, you guessed it")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    

# if guess == answer:
#     print("You guessed it for the first attempt")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed it")