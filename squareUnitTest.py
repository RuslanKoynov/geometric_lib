import unittest
from square import area
from square import perimeter

class CircleTest(unittest.TestCase):
    #test for area
    def test_for_area_first_integer(self):
        result = area(3)
        self.assertEqual(result, 9)

    def test_for_area_second_integer(self):
        result = area(20)
        self.assertEqual(result, 400)

    def test_for_area_first_float(self):
        result = area(3.5)
        self.assertEqual(result, 12.25)

    def test_for_area_second_float(self):
        result = area(6.31)
        self.assertEqual(result, 39.81609999999999)

    def test_for_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    #test for perimeter
    def test_for_perimeter_first_integer(self):
        result = perimeter(3)
        self.assertEqual(result, 12)

    def test_for_perimeter_second_integer(self):
        result = perimeter(20)
        self.assertEqual(result, 80)

    def test_for_perimeter_first_float(self):
        result = perimeter(3.5)
        self.assertEqual(result, 14)

    def test_for_perimeter_second_float(self):
        result = perimeter(6.31)
        self.assertEqual(result, 25.24)

    def test_for_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)