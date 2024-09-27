import unittest
from circle import area
from circle import perimeter

class CircleTest(unittest.TestCase):
    #test for area
    def test_for_area_first_integer(self):
        result = area(3)
        self.assertEqual(result, 28.274333882308138)

    def test_for_area_second_integer(self):
        result = area(20)
        self.assertEqual(result, 1256.6370614359173)

    def test_for_area_first_float(self):
        result = area(3.5)
        self.assertEqual(result, 38.48451000647496)

    def test_for_area_second_float(self):
        result = area(6.31)
        self.assertEqual(result, 125.08596725459655)

    def test_for_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    #test for perimeter
    def test_for_perimeter_first_integer(self):
        result = perimeter(3)
        self.assertEqual(result, 18.84955592153876)

    def test_for_perimeter_second_integer(self):
        result = perimeter(20)
        self.assertEqual(result, 125.66370614359172)

    def test_for_perimeter_first_float(self):
        result = perimeter(3.5)
        self.assertEqual(result, 21.991148575128552)

    def test_for_perimeter_second_float(self):
        result = perimeter(6.31)
        self.assertEqual(result, 39.64689928830319)

    def test_for_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)