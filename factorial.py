def factorial(n: int) -> int:
    """
    To find the factorial of the number `n`

    Args:
        n (int): The number to which `factorial` needs to be found

    Returns:
        int: factorial of the entered number `n`
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    
user=int(input("Enter integer : "))
print(factorial(user))