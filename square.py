import unittest

class SquareTestCase(unittest.TestCase):
    """Test function square
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
        self.assertEqual(get_square_area(0), 0)
        for x in [-2, 0, 9]:
            if x != 9:
                self.assertRaises(ValueError,square_area, x)

    def test_perimeter_zero_sides(self):
        """Test function for zero sides perimeter case
        """
    def test_area_negative_or_zero_values(self):
        """Test function for negativeor zero values area case
        """
        self.assertEqual(square_perimeter(0), 0)
        for x in [-2, 9, 0]:
            if x != 9:
                self.assertRaises(ValueError, square_area, x)

    def test_area_float_sides(self):
        """Test function for float sides area case
        """
    def test_area_float_values(self):
        """Test function for float sides values case
        """
        self.assertAlmostEqual(square_area(3.98), 33.5124 , 3)


    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """

    def test_perimeter_float_values(self):
        """Test function for float values perimeter case
        """
        self.assertEqual(square_perimeter(5.76), 22.365, 3)


    def test_area_int_values(self):
        """Test function for int values area case
        """
        self.assertEqual(square_area(9), 81)

    def test_perimeter_int_values(self):
        """Test function for int values perimeter case
        """
        self.assertEqual(square_perimeter(9), 36)

def square_area(a):
    """Takes the number a, returns the product of the number a and a.
    """
    return a * a

def square_perimeter(a):
    """Takes the number a, returns the number a multiplied by 4
    """
    return 4 * a
