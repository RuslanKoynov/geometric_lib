import unittest
import square
import triangle
import circle
import rectangle
import math

class TestLibrary(unittest.TestCase):
    
        # test for square area
    def test_squareArea(self):
        self.assertEqual(square.area(2),4)
        self.assertEqual(square.area(1000000),1000000000000)
        self.assertEqual(square.area(0),0)
        self.assertEqual(square.area("str"),"Wrong argument-type")
        self.assertEqual(square.area(-1),"Argumeng cant be <0")

        # test for triangle area
    def test_triangleArea(self):
        self.assertEqual(triangle.area(2,2),2)
        self.assertEqual(triangle.area(1000000,5000),2500000000)
        self.assertEqual(triangle.area(0,0),0)
        self.assertEqual(triangle.area("str",123),"Wrong argument-type")
        self.assertEqual(triangle.area(-1,32),"Argumeng cant be <0")

        # test for circle area
    def test_circleArea(self):
        self.assertEqual(circle.area(2),4 * math.pi)
        self.assertEqual(circle.area(1000000),1000000000000 * math.pi)
        self.assertEqual(circle.area(0),0)
        self.assertEqual(circle.area("str"),"Wrong argument-type")
        self.assertEqual(circle.area(-1),"Argumeng cant be <0")

        # test for rectangle area
    def test_rectangleArea(self):
        self.assertEqual(rectangle.area(2,2),4)
        self.assertEqual(rectangle.area(1000000,5000),5000000000)
        self.assertEqual(rectangle.area(0,0),0)
        self.assertEqual(rectangle.area("str",123),"Wrong argument-type")
        self.assertEqual(rectangle.area(-1,32),"Argumeng cant be <0")

        # test for square perimeter
    def test_squarePerimeter(self):
        self.assertEqual(square.perimeter(2),8)
        self.assertEqual(square.perimeter(1000000),4000000)
        self.assertEqual(square.perimeter(0),0)
        self.assertEqual(square.perimeter("str"),"Wrong argument-type")
        self.assertEqual(square.perimeter(-1),"Argumeng cant be <0")

        # test for triangle perimeter
    def test_trianglePerimeter(self):
        self.assertEqual(triangle.perimeter(2,2,2),6)
        self.assertEqual(triangle.perimeter(1000000,5000,20000),1025000)
        self.assertEqual(triangle.perimeter(0,0,0),0)
        self.assertEqual(triangle.perimeter(0,0,2),"Argumeng cant be <0 or if one arg = 0 other must be 0")
        self.assertEqual(triangle.perimeter(0,2,0),"Argumeng cant be <0 or if one arg = 0 other must be 0")
        self.assertEqual(triangle.perimeter(2,0,0),"Argumeng cant be <0 or if one arg = 0 other must be 0")
        self.assertEqual(triangle.perimeter("str",123,23),"Wrong argument-type")
        self.assertEqual(triangle.perimeter(-1,32,173),"Argumeng cant be <0 or if one arg = 0 other must be 0")

        # test for circle perimeter
    def test_circlePerimeter(self):
        self.assertEqual(circle.perimeter(2),4 * math.pi)
        self.assertEqual(circle.perimeter(1000000),2000000 * math.pi)
        self.assertEqual(circle.perimeter(0),0)
        self.assertEqual(circle.perimeter("str"),"Wrong argument-type")
        self.assertEqual(circle.perimeter(-1),"Argumeng cant be <0")

        # test for rectangle perimeter
    def test_rectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(2,2),8)
        self.assertEqual(rectangle.perimeter(1000000,5000),2010000)
        self.assertEqual(rectangle.perimeter(0,0),0)
        self.assertEqual(rectangle.perimeter(0,1),"Argumeng cant be <0 or only one be 0")
        self.assertEqual(rectangle.perimeter(1,0),"Argumeng cant be <0 or only one be 0")
        self.assertEqual(rectangle.perimeter("str",123),"Wrong argument-type")
        self.assertEqual(rectangle.perimeter(-1,32),"Argumeng cant be <0 or only one be 0")



if  __name__ == '__main__':
    unittest.main()