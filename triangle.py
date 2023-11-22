import unittest

class TriangleTestCase(unittest.TestCase):
    """Test function triangle
    """
    def set_up(self):
        """Set up fucntion
        """
        pass


    def test_area_zero_side_or_height(self):
        """Test function for zero side or height area case
        """
    def test_area_negative_or_zero_side_or_height(self):
        """Test function for negative or zero side or height area case
        """
        self.assertRaises(ValueError, triangle_area, x, y)
        self.assertRaises(ValueError, triangle_area, x, y)

    def test_perimeter_zero_side(self):
        """Test function for zero sides perimeter case
        """
    def test_perimeter_negative_or_zero_side(self):
        """Test function for negative or zero sides perimeter case
        """
        elf.assertRaises(ValueError, triangle_perimeter, x, y, z)
        elf.assertRaises(ValueError, triangle_perimeter, x, y, z)

    def test_area_float_sides_height(self):
        """Test function for float sides and float height area case
        """
        self.assertAlmostEqual(get_triangle_area(5.76, 1.34), 7.6542 , 3)
    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """
        self.assertEqual(get_triangle_perimeter(5.76, 1.39, 8.33), 15.893 , 3)

    def test_area_negative_values(self):
        """Test function for negative values area case
        """
        for x in [-2, 9]:
            for y in [-2, 9]:
                if [x, y] != [9, 9]:
                    self.assertRaises(ValueError, triangle_area, x, y)

    def test_perimeter_negative_values(self):
        """Test function for negative values area case
        """
        for x in [-2, 9, 8]:
            for y in [-2, 9, 8]:
                for z in [-2, 9, 8]:
                    if x < 0 or y < 0 or z < 0:
                        self.assertRaises(ValueError, triangle_perimeter, x, y, z)

    def test_area_int_values(self):
        """Test function for generic values area case
        """
        self.assertEqual(triangle_area(9, 4), 18)
    def test_perimeter_int_values(self):
        """Test function for generic values perimeter case
        """
        self.assertEqual(triangle_perimeter(9, 3, 3), 15)

def area(a, h):
    """Takes numbers a and h, returns their product divided by 2
    """
    return (a * h) / 2

def perimeter(a, b, c):
    """Accepts numbers a, b, c, returns the sum of these numbers
    """
    return a + b + c
