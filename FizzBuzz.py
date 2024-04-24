def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz Game
    
    Args:
        number (int): The `number` that needs to check

    Returns:
        str: `fizz` if the `number` is divisible by `3`
             `buzz` if the `number` is divisible by `5`
             `fizz buzz` if the `number` is divisible by `3` and `5`
             `number` as a string otherwise. 
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
    

for i in range(1, 101):
    if i % 2 != 0:
        print(fizz_buzz(i))
    elif i % 2 == 0:
        user_turn = input("It's your turn")
        if user_turn == fizz_buzz(i):
            continue
        else:
            print("You got wrong, Please try again")
            break