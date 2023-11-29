import unittest
import math

import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

# Тест 1: Проверка площади и периметра круга с положительным радиусом
r = 2
expected_area = math.pi * r * r
expected_perimeter = 2 * math.pi * r
actual_area = area(r)
actual_perimeter = perimeter(r)
print(f"Тест 1: r = {r}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 2: Проверка площади и периметра круга с отрицательным радиусом
r = -3
expected_area = math.pi * r * r
expected_perimeter = 2 * math.pi * r
actual_area = area(r)
actual_perimeter = perimeter(r)
print(f"Тест 2: r = {r}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 3: Проверка площади и периметра круга с нулевым радиусом
r = 0
expected_area = math.pi * r * r
expected_perimeter = 2 * math.pi * r
actual_area = area(r)
actual_perimeter = perimeter(r)
print(f"Тест 3: r = {r}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_yes(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_circle_area_no(self):
        res = area(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_area_real_numbers(self):
        res = area(4.25)
        self.assertEqual(res, 56.745017305465645)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_yes(self):
        res = perimeter(4)
        self.assertEqual(res, 25.132741228718345)

    def test_circle_perimeter_no(self):
        res = perimeter(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_perimeter_real_numbers(self):
        res = perimeter(4.25)
        self.assertEqual(res, 26.703537555513243)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
