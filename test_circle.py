import unittest
import circle

class TestCircle(unittest.TestCase):

    def test_area(self):
        result = round(circle.area(5), 2)
        self.assertEqual(result, 78.54)
        
    def test_perimeter(self):
        result = round(circle.perimeter(9), 2)
        self.assertEqual(result, 56.55)
        
    def test_perimeter(self):
        result = circle.perimeter(-9)
        self.assertEqual(result, 'Error')
