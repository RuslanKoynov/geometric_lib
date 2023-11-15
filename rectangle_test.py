import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_positive(self):
        res = area(5, 6)
        self.assertEqual(res, 30)

    def test_rectangle_area_negative(self):
        res = area(5, -6)
        self.assertEqual(res, 'Стороны прямоугольника не могут быть отрицательными')

    def test_rectangle_area_real(self):
        res = area(5.5, 6.6)
        self.assertEqual(res, 36.3)

    def test_rectangle_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_positive(self):
        res = perimeter(5, 6)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_negative(self):
        res = perimeter(5, -6)
        self.assertEqual(res, 'Стороны прямоугольника не могут быть отрицательными')

    def test_rectangle_perimeter_real(self):
        res = perimeter(5.5, 6.6)
        self.assertEqual(res, 24.2)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(5, 0)
        self.assertEqual(res, 10)

if __name__ == '__main__':
    unittest.main()
