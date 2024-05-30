import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(4, 6), 12)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()
