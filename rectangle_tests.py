import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6, 7)
        self.assertEqual(res, 42)

    def test_area_negative(self):
        res = area(10, -4)
        self.assertEqual(res,"None")

    def test_area_real(self):
        res = area(6.7, 7.6)
        self.assertEqual(res, 50.92)

    def test_area_zero(self):
        res = area(0, 7)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(6, 8)
        self.assertEqual(res, 28)

    def test_perimeter_negative(self):
        res = perimeter(5, -6)
        self.assertEqual(res, "None")

    def test_perimeter_real(self):
        res = perimeter(6.7, 7.6)
        self.assertEqual(res, 28.6)

    def test_perimeter_zero(self):
        res =  perimeter(5, 0)
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()

