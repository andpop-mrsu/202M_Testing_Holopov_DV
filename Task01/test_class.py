import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# ---------- Позитивные тесты ----------

def test_create_valid_triangle():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12
    assert t.triangle_type() == "nonequilateral"

def test_isosceles():
    t = Triangle(3, 3, 4)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 10

def test_equilateral():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15

def test_large_values():
    t = Triangle(10, 13, 15)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 38

def test_float_sides():
    t = Triangle(2.5, 2.5, 3.5)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 8.5

# ---------- Негативные тесты ----------

def test_invalid_triangle_equal_sum():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 4, 5)

def test_wrong_type_string():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 4, 5)

def test_invalid_triangle_large_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(5, 1, 1)


