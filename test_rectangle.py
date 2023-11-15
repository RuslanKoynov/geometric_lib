import unittest
def area(a, b):
    '''
    The area(a, b) function calculates the area of a rectangle.

    Formula:

    Area = a * b

    Description:

    •‎ Area is the area of the rectangle.
    •‎ a is the length of one side of the rectangle.
    •‎ b is the length of the other side of the rectangle.
    '''
    return a * b


def perimeter(a, b):
    '''
    The perimeter(a, b) function calculates the perimeter of a rectangle.
    Formula:

    Perimeter = 2 * (a + b)
    Descriprion:

    •‎ Perimeter is the perimeter of the rectangle.
    •‎ a is the length of one side of the rectangle.
    •‎ b is the length of the other side of the rectangle.
    '''
    return 2 * (a + b)

'''
Test for rectangle
'''
class RectangleTestCase(unittest.TestCase):
    def test_zero_dimensions(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_dimensions(self):
        res_area = area(4, 5)
        res_perimeter = perimeter(4, 5)
        self.assertEqual(res_area, 20)
        self.assertEqual(res_perimeter, 18)

if __name__ == '__main__':
    unittest.main()
