from circle import area, perimeter
import unittest

class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(12)
        self.assertEqual(res, 452.3893421169302)

    def test_area_real(self):
        res = area(16.25)
        self.assertEqual(res,829.5768100885547)

    def test_area_negative(self):
        res = area(-5)
        self.assertEqual(res,"Error")

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res,0.0)

    def test_perimeter_positive(self):
        res = perimeter(12)
        self.assertEqual(res,75.39822368615503)
    def test_perimeter_real(self):
        res = perimeter(16.25)
        self.assertEqual(res,102.10176124166827)

    def test_perimeter_negative(self):
        res = perimeter(-5)
        self.assertEqual(res,"Error")

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res,0.0)


if __name__ == '__main__':
    unittest.main()
