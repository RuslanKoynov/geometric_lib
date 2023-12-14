import unittest
import square

class TestSquare(unittest.TestCase):

    def test_area(self):
        result = square.area(2)
        self.assertEqual(result, 4)
        
    def test_perimeter(self):
        result = square.perimeter(2)
        self.assertEqual(result, 8)
        
    def test_negative_mul(self):
        self.assertRaises(TypeError, square.area, -10)
