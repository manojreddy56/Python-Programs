def calculate_hcf(a: int, b: int) -> int:
    """
    to find the hcf of two numbers a, b.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: the hcf of two numbers a, b
    """
    if a > b:
        small = b
    else:
        small = a
    
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf


def calculate_lcm(a: int, b: int) -> int:
    """
    To calculate the lcm of two numbers a, b.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: returns the lcm of two mumbers
    """
    hcf = calculate_hcf(a, b)
    lcm = a * b / hcf
    return lcm


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("HCF is: ",calculate_hcf(a, b))
print("LCM is: ",calculate_lcm(a, b))