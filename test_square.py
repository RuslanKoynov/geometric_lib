import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(4), 16)

if __name__ == '__main__':
    unittest.main()
