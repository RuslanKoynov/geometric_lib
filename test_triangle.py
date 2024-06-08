import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(4, 6), 12)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        
    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area(-4, 6)
        with self.assertRaises(ValueError):
            area(4, -6)
        with self.assertRaises(TypeError):
            area("four", 6)
        with self.assertRaises(TypeError):
            area(4, "six")
        with self.assertRaises(TypeError):
            area(None, 6)
            
    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)  # Invalid triangle
        with self.assertRaises(TypeError):
            perimeter("three", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "four", 5)

if __name__ == '__main__':
    unittest.main()
