import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_with_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_with_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_area_with_random_number(self):
        res=area(26,31)
        self.assertEqual(res,806)
    def test_perimeter_with_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_perimeter_with_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def test_perimeter_with_random_number(self):
        res=perimeter(26,31)
        self.assertEqual(res,114)

if __name__ == '__main__':
    unittest.main()



