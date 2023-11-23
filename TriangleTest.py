import unittest
from triangle import area
from triangle import perimeter

class TriangleTest(unittest.TestCase):
    #test for area
    def test_for_area_first_integer(self):
        result = area(3, 9)
        self.assertEqual(result, 13.5)

    def test_for_area_second_float(self):
        result = area(6.31, 9.87)
        self.assertEqual(result, 31.139849999999996)

    def test_for_area_zero(self):
        result = area(0, 9)
        self.assertEqual(result, 0)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('0', '91')

    #test for perimeter
    def test_for_perimeter_first_integer(self):
        result = perimeter(3, 9, 5)
        self.assertEqual(result, 17)

    def test_for_perimeter_second_float(self):
        result = perimeter(6.31, 9.87, 8.09)
        self.assertEqual(result, 24.27)

    def test_for_perimeter_zero(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    def test_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter('0', '10', '15')
