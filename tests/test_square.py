import unittest
import square
from contextlib import nullcontext as does_not_raise


class TestSquare(unittest.TestCase):
    def test_area(self):
        params = [
            (0.001, does_not_raise(), ''),
            (1234, does_not_raise(), ''),
            (0, self.assertRaises(ValueError), 'The side(a = 0) of a square must be greater than zero'),
            (-1, self.assertRaises(ValueError), 'The side(a = -1) of a square must be greater than zero'),
            ('ab', self.assertRaises(TypeError), 'The side of a square must be int or float')
        ]
        for a, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    self.assertEquals(square.area(a), a ** 2)
                if context is not None:
                    self.assertEquals(
                        exc_message,
                        str(context.exception)
                    )

    def test_perimeter(self):
        params = [
            (0.001, does_not_raise(), ''),
            (1234, does_not_raise(), ''),
            (0, self.assertRaises(ValueError), 'The side(a = 0) of a square must be greater than zero'),
            (-1, self.assertRaises(ValueError), 'The side(a = -1) of a square must be greater than zero'),
            ('ab', self.assertRaises(TypeError), 'The side of a square must be int or float')
        ]
        for a, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    self.assertEquals(square.perimeter(a), 4 * a)
                if context is not None:
                    self.assertEquals(
                        exc_message,
                        str(context.exception)
                    )
