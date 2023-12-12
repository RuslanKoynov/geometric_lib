import unittest
from traingle import area
from traingle import perimeter

class TraingleTestCase(unittest.TestCase):
    def test_area_with_zero(self):
        res = area(0,0)
        self.assertEqual(res, 0)

    def test_area_with_random_number1(self):
        res = area(10,2)
        self.assertEqual(res, 10)

    def test_area_with_random_number2(self):
        res=area(28,56)
        self.assertEqual(res, 784)

    def test_perimeter_with_zero(self):
        res = perimeter(0,0,0)
        self.assertEqual(res, 0)

    def test_perimeter_with_random_number2(self):
        res = perimeter(10,39,78)
        self.assertEqual(res, 127)

    def test_perimeter_with_random_number1(self):
        res=perimeter(31,982,65)
        self.assertEqual(res,1078)

if __name__ == '__main__':
    unittest.main()



