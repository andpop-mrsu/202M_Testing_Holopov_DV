class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника.

    Возвращает:
        "nonequilateral" — разносторонний
        "isosceles" — равнобедренный
        "equilateral" — равносторонний


    Позитивные тесты:
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'

    >>> get_triangle_type(3, 3, 4)
    'isosceles'

    >>> get_triangle_type(5, 5, 5)
    'equilateral'

    >>> get_triangle_type(7, 8, 9)
    'nonequilateral'

    >>> get_triangle_type(10, 10, 15)
    'isosceles'

    >>> get_triangle_type(2.5, 2.5, 3.5)
    'isosceles'


    Негативные тесты:
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides

    >>> get_triangle_type(0, 4, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides

    >>> get_triangle_type(-3, 4, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides

    >>> get_triangle_type("a", 4, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides

    >>> get_triangle_type(5, 1, 1)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides
    """

    sides = (a, b, c)

    if not all(isinstance(x, (int, float)) for x in sides):
        raise IncorrectTriangleSides

    if any(x <= 0 for x in sides):
        raise IncorrectTriangleSides

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides

    if a == b == c:
        return "equilateral"

    if a == b or a == c or b == c:
        return "isosceles"

    return "nonequilateral"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
