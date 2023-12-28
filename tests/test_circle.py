import unittest
import circle
from contextlib import nullcontext as does_not_raise


class TestCircle(unittest.TestCase):
    def test_area(self):
        eps = 0.1 ** 10
        params = [
            (0.001, 0.0000031415927, does_not_raise(), ''),
            (1234, 4783879.062809778, does_not_raise(), ''),
            (0, None, self.assertRaises(ValueError), 'The radius(a = 0) of a circle must be greater than zero'),
            (-1, None, self.assertRaises(ValueError), 'The radius(a = -1) of a circle must be greater than zero'),
            ('ab', None, self.assertRaises(TypeError), 'The radius of a circle must be int or float')
        ]
        for r, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = circle.area(r)
                if context is not None:
                    self.assertEquals(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )

    def test_perimeter(self):
        eps = 0.1 ** 10
        params = [
            (0.001, 0.0062831853072, does_not_raise(), ''),
            (1234, 7753.4506690596, does_not_raise(), ''),
            (0, None, self.assertRaises(ValueError), 'The radius(a = 0) of a circle must be greater than zero'),
            (-1, None, self.assertRaises(ValueError), 'The radius(a = -1) of a circle must be greater than zero'),
            ('ab', None, self.assertRaises(TypeError), 'The radius of a circle must be int or float')
        ]
        for r, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = circle.perimeter(r)
                if context is not None:
                    self.assertEquals(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )
