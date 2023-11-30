import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2

# Тест 1: Проверка площади и периметра прямоугольника с положительными значениями сторон
a = 2
b = 3
expected_area = 6
expected_perimeter = 10
actual_area = area(a, b)
actual_perimeter = perimeter(a, b)
print(f"Тест 1: a = {a}, b = {b}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 2: Проверка площади и периметра прямоугольника с отрицательными значениями сторон
a = -4
b = 5
expected_area = -20
expected_perimeter = 2
actual_area = area(a, b)
actual_perimeter = perimeter(a, b)
print(f"Тест 2: a = {a}, b = {b}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 3: Проверка площади и периметра прямоугольника с нулевыми значениями сторон
a = 0
b = 0
expected_area = 0
expected_perimeter = 0
actual_area = area(a, b)
actual_perimeter = perimeter(a, b)
print(f"Тест 3: a = {a}, b = {b}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()


from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_yes(self):
        res = area(4, 7)
        self.assertEqual(res, 28)

    def test_rectangle_area_no(self):
        res = area(4, -7)
        self.assertRaises(ExpectedException, aufuction, arg1, arg2)

    def test_rectangle_area_real_numbers(self):
        res = area(4.25, 7.36)
        self.assertEqual(res, 31.28)

    def test_rectangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_yes(self):
        res = perimeter(4, 7)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_no(self):
        res = perimeter(4, -7)
        self.assertRaises(ExpectedException, aufuction, arg1, arg2)

    def test_rectangle_perimeter_real_numbers(self):
        res = perimeter(4.25, 7.36)
        self.assertEqual(res, 23.22)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(4, 0)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
