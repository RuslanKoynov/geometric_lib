import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    """
    Test square function.
    """
    def test_square_area_integer(self):
        """
        Test the area function by integer.
        """
        # Test for side a = 4
        self.assertEqual(area(4), 16)
        
    def test_square_area_negative(self):
        """
        Test the area function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for side a = -6
           area(-6)

    def test_square_area_float(self):
        """
        Test the area function by float
        """
        # Test for side a = 6.9
        self.assertEqual(area(6.9), 6.9*6.9)
    
    def test_square_area_big(self):
        """
        Test the area function by float and int
        """
        # Test for side a = 52
        self.assertEqual(area(520), 520*520)
        
    
    def test_square_perimeter_integer(self):
        """
        Test the perimeter function by integer.
        """
        # Test for side a = 5
        self.assertEqual(perimeter(5), 20)


    def test_square_perimeter_float(self):
        """
        Test the area function by float
        """
        # Test for side a = 6.9
        self.assertEqual(perimeter(6.9), 4*6.9)
    
    def test_square_perimeter_big(self):
        """
        Test the area function by float and int
        """
        # Test for side a = 520
        self.assertEqual(perimeter(520), 4*520)
        
    def test_square_perimeter_negative(self):
        """
        Test the perimeter function by negeative integer.
        """
        with self.assertRaises(Exception):
            # Test for side a = -6
           perimeter(-6)

