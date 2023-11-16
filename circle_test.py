import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_positive(self):
        res = area(6)
        self.assertEqual(res, 113.09733552923255)

    def test_circle_area_negative(self):
        res = area(-6)
        self.assertRaises(res, Exception)

    def test_circle_area_real(self):
        res = area(6.5)
        self.assertEqual(res, 132.73228961416876)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_positive(self):
        res = perimeter(6)
        self.assertEqual(res, 37.69911184307752)

    def test_circle_perimeter_negative(self):
        res = perimeter(-6)
        self.assertRaises(res, Exception)

    def test_circle_perimeter_real(self):
        res = perimeter(6.5)
        self.assertEqual(res, 40.840704496667314)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()
