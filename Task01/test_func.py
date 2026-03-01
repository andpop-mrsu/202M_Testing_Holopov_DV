import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangleFunction(unittest.TestCase):

    # ---------- Позитивные тесты ----------

    def test_nonequilateral_basic(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_isosceles_basic(self):
        self.assertEqual(get_triangle_type(3, 3, 4), "isosceles")

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    def test_nonequilateral_large(self):
        self.assertEqual(get_triangle_type(7, 8, 9), "nonequilateral")

    def test_isosceles_large(self):
        self.assertEqual(get_triangle_type(10, 10, 15), "isosceles")

    def test_isosceles_float(self):
        self.assertEqual(get_triangle_type(2.5, 2.5, 3.5), "isosceles")


    # ---------- Негативные тесты ----------

    def test_invalid_triangle_equal_sum(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-3, 4, 5)

    def test_wrong_type_string(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 4, 5)

    def test_invalid_triangle_large_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 1, 1)


if __name__ == "__main__":
    unittest.main()
