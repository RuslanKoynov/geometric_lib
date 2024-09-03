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
        
    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area(-5, 3)
        with self.assertRaises(TypeError):
            area("five", 3)
        with self.assertRaises(TypeError):
            area(None, 3)
        with self.assertRaises(TypeError):
            area([5], 3)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 3)
        with self.assertRaises(TypeError):
            perimeter("five", 3)
        with self.assertRaises(TypeError):
            perimeter(None, 3)
        with self.assertRaises(TypeError):
            perimeter(5, None)
        with self.assertRaises(TypeError):
            perimeter([5], 3)
        with self.assertRaises(TypeError):
            perimeter(5, [3])

if __name__ == '__main__':
    unittest.main()
