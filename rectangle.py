import unittest
class RectangleTestCase(unittest.TestCase):
    """Test function rectangle
    """
    def set_up(self):
        """Set up fucntion
        """
        pass

    def test_area_zero_sides(self):
        """Test function for zero sides area case
        """
    def test_perimeter_negative_or_zero_values(self):
        """Test function for negative or zero values perimeter case
        """
        self.assertEqual(rectangle_area(0, 0), 0)
        for x in [-2, 0, 9]:
            for y in [-2, 0, 9]:
                if [x, y] != [9, 9]:
                    self.assertRaises(ValueError, rectangle_perimeter, x, y)

    def test_perimeter_zero_sides(self):
        """Test function for zero sides perimeter case
        """
    def test_area_negative_or_zero_values(self):
        """Test function for negativeor zero values area case
        """
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        for x in [-2, 9, 0]:
            for y in [-2, 9, 0]:
                if [x, y] != [9, 9]:
        self.assertRaises(ValueError, rectangle_area, x, y)

    def test_area_zero_side(self):
        """Test function for zero side area case
        """
    def test_area_float_values(self):
        """Test function for float values area case
        """
        self.assertEqual(rectangle_area(0, 9), 0)
        self.assertEqual(rectangle_area(9, 0), 0)
        self.assertAlmostEqual(rectangle_area(5.31, 3.98), 18.98319, 3)

    def test_perimeter_zero_side(self):
        """Test function for zero side perimeter case
        """
    def test_perimeter_float_values(self):
        """Test function for float values perimeter case
        """
        self.assertEqual(rectangle_perimeter(0, 9), 0)
        self.assertEqual(rectangle_perimeter(9, 0), 0)
        self.assertEqual(rectangle_perimeter(5.72, 9.16), 29.31 , 3)

    def test_area_float_sides(self):
        """Test function for float sides area case
        """
    def test_area_int_values(self):
        """Test function for int values area case
        """
        self.assertAlmostEqual(rectangle_area(4.23, 6.82), 28.8486, 3)
        self.assertEqual(rectangle_area(9, 3), 24)

    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """
    def test_perimeter_int_values(self):
        """Test function for int values perimeter case
        """
        self.assertEqual(rectangle_perimeter(5.72, 9.16), 29.31, 3)
        self.assertEqual(rectangle_perimeter(9, 3), 24)
def rectangle_area(a, b):
    """Takes numbers a and b and returns their product
    """
    return a * b 

def rectangle_perimeter(a, b):
    """Takes numbers a and b, returns their sum divided by 2
    """
    return (a + b)*2 
