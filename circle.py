import math
import unittest

class CircleTestCase(unittest.TestCase):
    """Test functions Circle
    """
    def set_up(self):
        """Set up fucntion
        """
        pass

        def test_area_zero_rad(self):
            """Test function for zero radius area case
            """
            self.assertEqual(circle_area(0), 0)

        def test_circumference_zero_rad(self):
            """Test function for zero radius circumference case
            """
            self.assertEqual(circle_perimeter(0), 0)

        def test_area_negative_rad(self):
            """Test function for negative radius area case
            """
        def test_area_negative_or_zero_value(self):
            """Test function for negative or zero radius area case
            """
            self.assertRaises(ValueError, circle_area, 0)
            self.assertRaises(ValueError, circle_area, -2)

        def test_circumference_negative_rad(self):
            """Test function for negative radius circumference case
            """
        def test_circumference_negative_or_zero_rad(self):
            """Test function for negative or zero radius circumference case
            """
        self.assertRaises(ValueError, circle_perimeter, 0)
        self.assertRaises(ValueError, circle_perimeter, -2)

        def test_area_float_rad(self):
            """Test function for float radius area case
            """
            self.assertAlmostEqual(circle_area(5.76), 104.177664, 8)

        def test_circumference_float_rad(self):
            """Test function for float radius circumference case
            """
            self.assertAlmostEqual(circle_perimeter(5.76), 36.19113984, 8)

        def test_area_int_rad(self):
            """Test function for int radius area case
            """
            self.assertAlmostEqual(circle_area(9), 254.3442819, 5)

        def test_circumference_int_rad(self):
            """Test function for int radius area case
            """
            self.assertAlmostEqual(circle_perimeter(9), 56.548656 , 5)


def circle_area(r):
    """Takes the number r, returns the number r squared multiplied by pi
    """
    return math.pi * r * r


def circle_perimeter(r):
    """Takes the number r, returns the number r multiplied by 2 and pi
    """
    return 2 * math.pi * r

