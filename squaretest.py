import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_with_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_with_square(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_with_random_number(self):
        res=area(28)
        self.assertEqual(res, 784)

    def test_perimeter_with_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_with_square(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_with_random_number(self):
        res=perimeter(31)
        self.assertEqual(res,124)

if __name__ == '__main__':
    unittest.main()



