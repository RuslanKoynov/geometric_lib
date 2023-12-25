import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_rational_area(self):
        res = area(3.5)
        self.assertAlmostEqual(res, 38.484, delta=0.001)

    def test_circle_negative_area(self):
        self.assertRaises(TypeError, area, -3)

    def test_circle_positive_area(self):
        res = area(3)
        self.assertAlmostEqual(res, 28.274, delta=0.001)

    def test_circle_other_data_type_area(self):
        self.assertRaises(TypeError, area, "123")

    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_rational_perimeter(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 21.991, delta=0.001)

    def test_circle_negative_perimeter(self):
        self.assertRaises(TypeError, perimeter, -3)

    def test_circle_positive_perimeter(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 18.849,delta=0.001)

    def test_circle_other_data_type_perimeter(self):
        self.assertRaises(TypeError, perimeter, "123")

if __name__ == '__main__':
    unittest.main()
