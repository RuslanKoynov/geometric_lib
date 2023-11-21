from rectangle import area, perimeter
import unittest

class RectangleTestCase(unittest.TestCase):

    def test_area_positive(self):
        res = area(11,22)
        self.assertEqual(res,242)

    def test_area_negative(self):
        res = area(-5,-3)
        self.assertEqual(res,"Error")

    def test_area_zero(self):
        res = area(0,0)
        self.assertEqual(res,0.0)

    def test_area_real(self):
        res = area(54.23,65.12)
        self.assertEqual(res,3531.4576)

    def test_perimeter_positive(self):
        res = perimeter(123,543)
        self.assertEqual(res,1332)

    def test_perimeter_negative(self):
        res = perimeter(-234,-123)
        self.assertEqual(res,"Error")

    def test_perimeter_zero(self):
        res = perimeter(0,0)
        self.assertEqual(res,0.0)

    def test_perimeter_real(self):
        res = perimeter(324.123,5.23)
        self.assertEqual(res,658.706)

if __name__ == '__main__':
    unittest.main()