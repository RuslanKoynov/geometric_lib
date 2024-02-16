import unittest
import rectangle
from contextlib import nullcontext as does_not_raise


class TestRectangle(unittest.TestCase):
    def test_area(self):
        eps = 0.1 ** 5
        params = [
            (0.001, 10, 0.01, does_not_raise(), ''),
            (15, 0.001, 0.015, does_not_raise(), ''),
            (0, 10, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (10, 0, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (-1, 10, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (10, -1, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            ('ab', 10, None, self.assertRaises(TypeError), 'The sides of a rectangle must be int or float'),
            (10, 'ab', None, self.assertRaises(TypeError), 'The sides of a rectangle must be int or float')
        ]
        for a, b, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = rectangle.area(a, b)
                if context is not None:
                    self.assertEqual(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )

    def test_perimeter(self):
        eps = 0.1 ** 5
        params = [
            (0.001, 10, 20.002, does_not_raise(), ''),
            (15, 0.001, 30.002, does_not_raise(), ''),
            (0, 10, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (10, 0, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (-1, 10, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            (10, -1, None, self.assertRaises(ValueError), 'The sides of a rectangle must be greater than zero'),
            ('ab', 10, None, self.assertRaises(TypeError), 'The sides of a rectangle must be int or float'),
            (10, 'ab', None, self.assertRaises(TypeError), 'The sides of a rectangle must be int or float')
        ]
        for a, b, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = rectangle.perimeter(a, b)
                if context is not None:
                    self.assertEqual(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )
