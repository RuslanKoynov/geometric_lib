import unittest
from circle import area
from circle import perimeter
import math


class CircleTestCase(unittest.TestCase):
    """
    Test circle function.
    """
    def test_circle_area_integer(self):
        """
        Test the area function by integer.
        """
        # Test for radius r = 2
        self.assertEqual(area(2), math.pi * 2 * 2)
    
    def test_circle_area_negative(self):
        """
        Test the area function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for radius r = -6
            area(-6)

    def test_circle_area_float(self):
        """
        Test the area function by float
        """
        # Test for radius r = 6.9
        self.assertEqual(area(6.9), math.pi * 6.9 * 6.9)
    
    def test_circle_area_big(self):
        """
        Test the area function by big
        """
        # Test for radius r = 100
        self.assertEqual(area(100), math.pi * 100 * 100)
        
    def test_circle_perimeter_integer(self):
        """
        Test the perimeter function by integer.
        """
        # Test for radius r = 2
        self.assertEqual(perimeter(2), 2 * math.pi * 2)

    def test_circle_perimeter_float(self):
        """
        Test the perimeter function by float
        """
        # Test for radius r = 6.9
        self.assertEqual(perimeter(6.9), 2 * math.pi * 6.9)
        
    def test_circle_perimeter_negative(self):
        """
        Test the area function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for radius r = -6
            perimeter(-6)
    
    def test_circle_perimeter_big(self):
        """
        Test the perimeter function by big
        """
        # Test for radius r = 100
        self.assertEqual(perimeter(100), 2 * math.pi * 100)
        
