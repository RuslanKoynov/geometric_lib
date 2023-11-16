import unittest
import triangle

class TestTriangle(unittest.TestCase):
    
    def test_area(self):
        result = triangle.area(4, 5)
        self.assertEqual(result, 10)
        
    def test_perimeter(self):
        result = triangle.perimeter(4, 5, 6)
        self.assertEqual(result, 15)
        
    def test_perimeter(self):
        result = triangle.perimeter('a', 'b', 'c')
        self.assertEqual(result, 15)
