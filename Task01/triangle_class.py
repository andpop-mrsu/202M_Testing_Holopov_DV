class IncorrectTriangleSides(Exception):
    pass


class Triangle:

    def __init__(self, a, b, c):
        sides = (a, b, c)

        if not all(isinstance(x, (int, float)) for x in sides):
            raise IncorrectTriangleSides

        if any(x <= 0 for x in sides):
            raise IncorrectTriangleSides

        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"

        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"

        return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
