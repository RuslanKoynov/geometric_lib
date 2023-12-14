import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class CircleTests(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)

    def test_circle_perimeter(self):
        self.assertEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(1), 6.283185307179586)
        self.assertAlmostEqual(circle_perimeter(5), 31.41592653589793)

class RectangleTests(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(0, 0), 0)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(5, 6), 30)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(4, 0), 8)
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 6), 22)

class SquareTests(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(3), 9)
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimeter(5), 20)

class TriangleTests(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle_area(0, 0), 0)
        self.assertEqual(triangle_area(4, 3), 6)  
        self.assertEqual(triangle_area(5, 2), 5) 

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(triangle_perimeter(3, 4, 5), 12) 
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)  

if __name__ == '__main__':
    unittest.main()
