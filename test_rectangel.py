import unittest
from rectangle import perimeter
from rectangle import area


class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        """
        Test the area function.
        """
        # Test for sides a = 10, b = 5
        self.assertEqual(area(10, 5), 50) 
        # Test for sides a = 15.2, b = 3.3
        self.assertAlmostEqual(area(15.2, 3.3), 15.2*3.3)
        # Test for sides a = 20, b = 50.2
        self.assertAlmostEqual(area(20, 50.2), 20*50.2)

    def test_perimeter(self):
        """
        Test the perimeter function.
        """
        # Test for sides a = 10, b = 5
        self.assertAlmostEqual(perimeter(10, 5), 30)
        # Test for sides a = 15.2, b = 3.3
        self.assertAlmostEqual(perimeter(15.2, 3.3), 2*(15.2+3.3))
        # Test for sides a = 20, b = 50.2
        self.assertAlmostEqual(perimeter(20, 50.2), 2*(50.2+20))
