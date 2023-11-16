import unittest
import circle
import rectangle
import square
import triangle

class MyTestCase(unittest.TestCase):

    def test_rectangle_positive(self):
        self.assertEqual(rectangle.area(12, 8), 96)
        self.assertEqual(rectangle.area(15, 4), 60)
        self.assertEqual(rectangle.area(7, 11), 77)

    def test_rectangle_area_not_positive(self):
        self.assertEqual(rectangle.area(12, 0), -1)
        self.assertEqual(rectangle.area(0, 7), -1)
        self.assertEqual(rectangle.area(0, 0), -1)

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(6, 4), 20)
        self.assertEqual(rectangle.perimeter(8, 2), 20)
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_rectangle_perimeter_not_positive(self):
        self.assertEqual(rectangle.perimeter(0, 0), -1)
        self.assertEqual(rectangle.perimeter(0, 6), -1)
        self.assertEqual(rectangle.perimeter(6, 0), -1)
        self.assertEqual(rectangle.perimeter(-6, 6), -1)
        self.assertEqual(rectangle.perimeter(6, -6), -1)

    def test_circle_perimeter_positive(self):
        self.assertEqual(circle.perimeter(2), 12.566370614359172)

    def test_circle_perimeter_not_positive(self):
        self.assertEqual(circle.perimeter(-2), -1)
        self.assertEqual(circle.perimeter(0), -1)

    def test_circle_area_positive(self):
        self.assertEqual(circle.area(2), 12.566370614359172)

    def test_circle_area_not_positive(self):
        self.assertEqual(circle.area(-2), -1)
        self.assertEqual(circle.area(0), -1)

    def test_square_perimeter_positive(self):
        self.assertEqual(square.perimeter(8), 32)
        self.assertEqual(square.perimeter(7), 28)

    def test_square_perimeter_not_positive(self):
        self.assertEqual(square.perimeter(-2), -1)
        self.assertEqual(square.perimeter(0), -1)

    def test_square_area_positive(self):
        self.assertEqual(square.area(6), 36)
        self.assertEqual(square.area(9), 81)

    def test_square_area_not_positive(self):
        self.assertEqual(square.area(-3), -1)
        self.assertEqual(square.area(0), -1)

    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
        self.assertEqual(triangle.perimeter(6, 8, 10), 24)

    def test_triangle_perimeter_not_positive(self):
        self.assertEqual(triangle.perimeter(-2, 4, 4), -1)
        self.assertEqual(triangle.perimeter(4, -2, 4), -1)
        self.assertEqual(triangle.perimeter(4, 4, -2), -1)
        self.assertEqual(triangle.perimeter(0, 4, 4), -1)
        self.assertEqual(triangle.perimeter(4, 0, 4), -1)
        self.assertEqual(triangle.perimeter(4, 4, 0), -1)

    def test_triangle_area_positive(self):
        self.assertEqual(triangle.area(4, 3), 6)
        self.assertEqual(triangle.area(5, 2), 5)

    def test_triangle_area_not_positive(self):
        self.assertEqual(triangle.area(-2, 3), -1)
        self.assertEqual(triangle.area(3, -2), -1)
        self.assertEqual(triangle.area(0, 3), -1)
        self.assertEqual(triangle.area(3, 0), -1)
        self.assertEqual(triangle.area(0, 0), -1)

    def test_correct_triangle(self):
        self.assertEqual(triangle.perimeter(2, 2, 5), -1)
        self.assertEqual(triangle.perimeter(2, 5, 2), -1)
        self.assertEqual(triangle.perimeter(5, 2, 2), -1)

if __name__ == '__main__':
    unittest.main()

