import unittest
import triangle
import rectangle
import square
import circle

class TriangleTestCase(unittest.TestCase):
    def test_area_triangle(self):
        result_1 = triangle.area(6, 8)
        self.assertEqual(result_1, 24)

        result_2 = triangle.area(10, 15)
        self.assertEqual(result_2, 75)

        result_3 = triangle.area(3.5, 7)
        self.assertEqual(result_3, 12.25)

        result_4 = triangle.area(9.2, 4.6)
        self.assertEqual(result_4, 21.159999999999997)

        result_5 = triangle.area(0, 0)
        self.assertEqual(result_5, 0)

        result_6 = triangle.area(0, 3)
        self.assertEqual(result_6, 0)

        result_7 = triangle.area(3, 0)
        self.assertEqual(result_7, 0)

        result_8 = triangle.area(1000000000, 2000000000)
        self.assertEqual(result_8, 1000000000000000000)

    def test_perimeter_triangle(self):
        result_1 = triangle.perimeter(3, 4, 5)
        self.assertEqual(result_1, 12)

        result_2 = triangle.perimeter(8, 15, 17)
        self.assertEqual(result_2, 40)

        result_3 = triangle.perimeter(2.5, 3, 4.5)
        self.assertEqual(result_3, 10)

        result_4 = triangle.perimeter(9, 12, 15)
        self.assertEqual(result_4, 36)

        result_5 = triangle.perimeter(0, 0, 0)
        self.assertEqual(result_5, 0)

        result_6 = triangle.perimeter(1000000000, 2000000000, 3000000000)
        self.assertEqual(result_6, 6000000000)
    
    def test_area_triangle_with_strings(self):
        with self.assertRaises(TypeError):
            result = triangle.area("a", 5)

        with self.assertRaises(TypeError):
            result = triangle.area(3, "b")

        with self.assertRaises(TypeError):
            result = triangle.area("c", "d")

    def test_perimeter_triangle_with_strings(self):
        with self.assertRaises(TypeError):
            result = triangle.perimeter("a", 5, 6)

        with self.assertRaises(TypeError):
            result = triangle.perimeter(3, "b", 6)

        with self.assertRaises(TypeError):
            result = triangle.perimeter(3, 5, "c")
    
class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        result_1 = rectangle.area(3, 7)
        self.assertEqual(result_1, 21)

        result_2 = rectangle.area(-8, 12)
        self.assertEqual(result_2, -96)

        result_3 = rectangle.area(2.5, 6)
        self.assertEqual(result_3, 15)

        result_4 = rectangle.area(4.8, -9.2)
        self.assertEqual(result_4, -44.16)

        result_5 = rectangle.area(0, 0)
        self.assertEqual(result_5, 0)

        result_6 = rectangle.area(1000000000, 2000000000)
        self.assertEqual(result_6, 2e18)

    def test_perimeter_rectangle(self):
        result_1 = rectangle.perimeter(3, 7)
        self.assertEqual(result_1, 20)

        result_2 = rectangle.perimeter(-8, 12)
        self.assertEqual(result_2, 8)

        result_3 = rectangle.perimeter(2.5, 6)
        self.assertEqual(result_3, 17)

        result_4 = rectangle.perimeter(4.8, -9.2)
        self.assertEqual(result_4, -8.799999999999999)

        result_5 = rectangle.perimeter(0, 0)
        self.assertEqual(result_5, 0)

        result_6 = rectangle.area(0, 2)
        self.assertEqual(result_6, 0)

        result_7 = rectangle.area(5, 0)
        self.assertEqual(result_7, 0)

        result_8 = rectangle.area(10, 10)
        self.assertEqual(result_8, 100)

        result_9 = rectangle.perimeter(1000000000, 2000000000)
        self.assertEqual(result_9, 6000000000)

    def test_area_rectangle_with_strings(self):
        result_1 = rectangle.area("b", 6)
        self.assertEqual(result_1, "bbbbbb")

        result_2 = rectangle.area(4, "c")
        self.assertEqual(result_2, "cccc")

        with self.assertRaises(TypeError):
            result_3 = rectangle.area("d", "e")

    def test_perimeter_rectangle_with_strings(self):
        result_1 = rectangle.area("b", 6)
        self.assertEqual(result_1, "bbbbbb")

        result_2 = rectangle.area(4, "c")
        self.assertEqual(result_2, "cccc")

        with self.assertRaises(TypeError):
            result = rectangle.area("d", "e")

class SquareTestCase(unittest.TestCase):
    def test_area_square(self):
        result_1 = square.area(5)
        self.assertEqual(result_1, 25)

        result_2 = square.area(-10)
        self.assertEqual(result_2, 100)

        result_3 = square.area(2.5)
        self.assertEqual(result_3, 6.25)

        result_4 = square.area(3.8)
        self.assertEqual(result_4, 14.44)

        result_5 = square.area(0)
        self.assertEqual(result_5, 0)

        result_6 = square.area(1000000000)
        self.assertEqual(result_6, 1e18)

    def test_perimeter_square(self):
        result_1 = square.perimeter(5)
        self.assertEqual(result_1, 20)

        result_2 = square.perimeter(-10)
        self.assertEqual(result_2, -40)

        result_3 = square.perimeter(2.5)
        self.assertEqual(result_3, 10)

        result_4 = square.perimeter(3.8)
        self.assertEqual(result_4, 15.2)

        result_5 = square.perimeter(0)
        self.assertEqual(result_5, 0)

        result_6 = square.perimeter(1000000000)
        self.assertEqual(result_6, 4000000000)

    def test_area_square_with_strings(self):
        with self.assertRaises(TypeError):
            result = square.area("ab")

        with self.assertRaises(TypeError):
            result = square.area("abc")

    def test_perimeter_square_with_strings(self):
        result_1 = square.perimeter("a")
        self.assertEqual(result_1, "aaaa")

        result_2 = square.perimeter("abc")
        self.assertEqual(result_2, "abcabcabcabc")
        
class CircleTestCase(unittest.TestCase):
    def test_area_circle(self):
        result_1 = circle.area(3)
        self.assertEqual(result_1, 28.274333882308138)

        result_2 = circle.area(-7)
        self.assertEqual(result_2, 153.93804002589985)

        result_3 = circle.area(2.2)
        self.assertEqual(result_3, 15.205308443374602)

        result_4 = circle.area(-5.6)
        self.assertEqual(result_4, 98.52034561657591)

        result_5 = circle.area(0)
        self.assertEqual(result_5, 0)

        result_6 = circle.area(1000000000)
        self.assertEqual(result_6, 3.1415926535897933e+18)
    
    def test_perimeter_circle(self):
        result_1 = circle.perimeter(3)
        self.assertEqual(result_1, 18.84955592153876)

        result_2 = circle.perimeter(-7)
        self.assertEqual(result_2, -43.982297150257104)

        result_3 = circle.perimeter(2.2)
        self.assertEqual(result_3, 13.823007675795091)

        result_4 = circle.perimeter(-5.6)
        self.assertEqual(result_4, -35.18583772020568)

        result_5 = circle.perimeter(0)
        self.assertEqual(result_5, 0)

        result_6 = circle.perimeter(1000000000)
        self.assertEqual(result_6, 6283185307.179586)

    def test_area_circle_with_strings(self):
        with self.assertRaises(TypeError):
            result = circle.area("a")

        with self.assertRaises(TypeError):
            result = circle.area("abc")

    def test_perimeter_circle_with_strings(self):
        with self.assertRaises(TypeError):
            result = circle.perimeter("a")

        with self.assertRaises(TypeError):
            result = circle.perimeter("abc")
