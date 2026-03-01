import math


def solve_quadratic(a, b, c):
    """
    Возвращает корни квадратного уравнения ax^2 + bx + c = 0
    в порядке возрастания.
    """
    if a == 0 and b == 0 and c == 0:
        return ("infinity")
    
    if a == 0 and b == 0 and c != 0:
        return ("None")
    
    if a == 0:
        x = -c / b
        return (x,)

    d = b ** 2 - 4 * a * c

    if d < 0:
        return ()

    if d == 0:
        x = -b / (2 * a)
        return (x,)

    sqrt_d = math.sqrt(d)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)

    return (min(x1, x2), max(x1, x2))

#print(solve_quadratic(0, 0, 0))
