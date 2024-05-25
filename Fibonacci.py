def fibonacci(n: int) -> int:
    """Returns `n`th fibonacci number, for a positive `n`."""
    if n == 0  or n == 1:
        return n
    
    n_minus_2 = 0
    n_minus_1 = 1
    for n in range(n - 1):
        result = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = result
    
    return result


print(fibonacci(9))