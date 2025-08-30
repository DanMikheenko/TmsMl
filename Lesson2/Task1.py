import math


def calculate_quadratic_equation(a: int, b: int, c: int) -> tuple:
    """
    The function calculates a quadratic equation

    Args: 
        a: coefficient next to x^2
        b: coefficient next to x
        c: coefficient without x

    Returns
        the roots
    """

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return
    elif discriminant == 0:
        return -b/(2*a)
    else:
        first_root = (-b + math.sqrt(discriminant))/2*a
        second_root = (-b - math.sqrt(discriminant))/2*a
        return (first_root, second_root)

print(calculate_quadratic_equation(1, 4, -5))