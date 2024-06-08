import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(4), 16)
        
    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(TypeError):
            area("four")
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            area([4])

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-1)
        with self.assertRaises(TypeError):
            perimeter("four")
        with self.assertRaises(TypeError):
            perimeter(None)
        with self.assertRaises(TypeError):
            perimeter([4])

if __name__ == '__main__':
    unittest.main()
