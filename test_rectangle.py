import unittest
import rectangle

class TestRectangle(unittest.TestCase):

    def test_area(self):
        result = rectangle.area(4, 5)
        self.assertEqual(result, 20)
        
    def test_perimeter(self):
        result = rectangle.perimeter(4, 5)
        self.assertEqual(result, 18)
        
    def test_negative_mul(self):
        self.assertRaises(TypeError, rectangle.area, -10, -5)
