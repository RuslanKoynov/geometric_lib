import unittest

def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

# Тест 1: Проверка площади и периметра треугольника с положительными значениями основания и высоты
a = 3
h = 4
b = 5
c = 6
expected_area = a * h / 2
expected_perimeter = a + b + c
actual_area = area(a, h)
actual_perimeter = perimeter(a, b, c)
print(f"Тест 1: a = {a}, h = {h}, b = {b}, c = {c}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 2: Проверка площади и периметра треугольника с отрицательными значениями основания и высоты
a = -2
h = -3
b = -4
c = -5
expected_area = a * h / 2
expected_perimeter = a + b + c
actual_area = area(a, h)
actual_perimeter = perimeter(a, b, c)
print(f"Тест 2: a = {a}, h = {h}, b = {b}, c = {c}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 3: Проверка площади и периметра треугольника с нулевыми значениями основания и высоты
a = 0
h = 0
b = 0
c = 0
expected_area = a * h / 2
expected_perimeter = a + b + c
actual_area = area(a, h)
actual_perimeter = perimeter(a, b, c)
print(f"Тест 3: a = {a}, h = {h}, b = {b}, c = {c}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_yes(self):
        res = area(2, 8)
        self.assertEqual(res, 8)

    def test_triangle_area_no(self):
        res = area(2, -8)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_area_real_numbers(self):
        res = area(2.75, 8.6)
        self.assertEqual(res, 11.825)

    def test_triangle_area_zero(self):
        res = area(2, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_yes(self):
        res = perimeter(2, 8, 11)
        self.assertEqual(res, 21)

    def test_triangle_perimeter_no(self):
        res = perimeter(2, -8, 11)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_perimeter_real_numbers(self):
        res = perimeter(2.75, 8.6, 11)
        self.assertEqual(res, 22.35)

    def test_triangle_perimeter_zero(self):
        res = perimeter(2, 0, 8.59)
        self.assertEqual(res, 10.59)

if __name__ == '__main__':
    unittest.main()
