import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    """
    Test triangle function.
    """
    def test_triangle_area_integer(self):
        """
        Test the area function by integer.
        """
        # Test for side a = 6, height = 4
        self.assertEqual(area(6, 4), 12)
    
    def test_triangle_area_negative(self):
        """
        Test the area function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for side a = -6, height = -4
            area(-6, -4)

    def test_triangle_area_float(self):
        """
        Test the area function by float
        """
        # Test for side a = 6.9, height = 5.2
        self.assertEqual(area(6.9, 5.2), 6.9*5.2/2)
    
    def test_triangle_area_float_int(self):
        """
        Test the area function by float and int
        """
        # Test for side a = 7.7, height = 10
        self.assertEqual(area(7.7, 10), 7.7*10/2)
        
    
    def test_triangle_perimeter_integer(self):
        """
        Test the perimeter function by integer.
        """
        # Test for sides a = 7, b = 5, c = 6
        self.assertEqual(perimeter(7, 5, 6), 18)


    def test_triangle_perimeter_float(self):
        """
        Test the perimeter function by float
        """
        # Test for sides a = 5.2, b = 4,6, c = 10.2
        self.assertEqual(perimeter(5.2, 4.6, 10.2), 20)
    
    def test_triangle_perimeter_float_int(self):
        """
        Test the perimeter function by float and int
        """
               # Test for sides a = 6.9, b = 228, c = 281.1
        self.assertEqual(perimeter(6.9, 228, 281.1), 516)
    
    def test_triangle_perimeter_negative(self):
        """
        Test the perimeter function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for side a = -6, b = -4, c = -5
            perimeter(-6, -4, -5)
 
