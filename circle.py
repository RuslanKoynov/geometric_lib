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
print("error")

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

class CircleTests(unittest.TestCase):
    def test_area(self):
        # Проверяем правильность вычисления площади круга
        self.assertEqual(area(2), math.pi * 2 * 2)  # Входные данные: r = 2; Ожидаемый результат: pi * 2 * 2; Фактический результат: pi * 2 * 2
        self.assertEqual(area(4), math.pi * 4 * 4)  # Входные данные: r = 4; Ожидаемый результат: pi * 4 * 4; Фактический результат: pi * 4 * 4
        self.assertEqual(area(0), math.pi * 0 * 0)  # Входные данные: r = 0; Ожидаемый результат: pi * 0 * 0; Фактический результат: pi * 0 * 0

    def test_perimeter(self):
        # Проверяем правильность вычисления длины окружности
        self.assertEqual(perimeter(2), 2 * math.pi * 2)  # Входные данные: r = 2; Ожидаемый результат: 2 * pi * 2; Фактический результат: 2 * pi * 2
        self.assertEqual(perimeter(4), 2 * math.pi * 4)  # Входные данные: r = 4; Ожидаемый результат: 2 * pi * 4; Фактический результат: 2 * pi * 4
        self.assertEqual(perimeter(0), 2 * math.pi * 0)  # Входные данные: r = 0; Ожидаемый результат: 2 * pi * 0; Фактический результат: 2 * pi * 0

    def test_area_with_large_number(self):
        # Проверяем правильность вычисления площади круга с очень большим числом
        self.assertEqual(area(1000000), math.pi * 1000000 * 1000000)  # Входные данные: r = 1000000; Ожидаемый результат: pi * 1000000 * 1000000; Фактический результат: pi * 1000000 * 1000000

    def test_perimeter_with_large_number(self):
        # Проверяем правильность вычисления длины окружности с очень большим числом
        self.assertEqual(perimeter(1000000), 2 * math.pi * 1000000)  # Входные данные: r = 1000000; Ожидаемый результат: 2 * pi * 1000000; Фактический результат: 2 * pi * 1000000

if __name__ == '__main__':
    unittest.main()