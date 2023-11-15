import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_positive(self):
        res = area(5, 6)
        self.assertEqual(res, 15)

    def test_triangle_area_negative(self):
        res = area(5, -6)
        self.assertEqual(res, 'Основание и высота не могут быть отрицательными')

    def test_triangle_area_real(self):
        res = area(5.5, 6.6)
        self.assertEqual(res, 18.15)

    def test_triangle_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_positive(self):
        res = perimeter(5, 6, 7)
        self.assertEqual(res, 18)

    def test_triangle_perimeter_negative(self):
        res = perimeter(5, -6, 4)
        self.assertEqual(res, 'Стороны треугольника не могут быть отрицательными')

    def test_triangle_perimeter_real(self):
        res = perimeter(5.5, 6.6, 10)
        self.assertEqual(res, 22.1)

    def test_triangle_perimeter_zero(self):
        res = perimeter(5, 0, 5.5)
        self.assertEqual(res, 10.5)


if __name__ == '__main__':
    unittest.main()
