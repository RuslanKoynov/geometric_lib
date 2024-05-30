import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_normal(self):
        self.assertEqual(area(5, 3), 15)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 3), 16)

if __name__ == '__main__':
    unittest.main()
