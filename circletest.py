import math
import unittest
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_with_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_with_square(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_area_with_random_number(self):
        res=area(28)
        self.assertEqual(res, 2463.0086404143976)

    def test_perimeter_with_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_with_square(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_with_random_number(self):
        res=perimeter(31)
        self.assertEqual(res,194.77874452256717)

if __name__ == '__main__':
    unittest.main()



