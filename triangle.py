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

class TriangleTests(unittest.TestCase):
    def test_area(self):
        # Проверяем правильность вычисления площади треугольника
        self.assertEqual(area(2, 3), 3)  # Входные данные: a = 2, h = 3; Ожидаемый результат: 3; Фактический результат: 3
        self.assertEqual(area(4, 5), 10)  # Входные данные: a = 4, h = 5; Ожидаемый результат: 10; Фактический результат: 10
        self.assertEqual(area(0, 0), 0)  # Входные данные: a = 0, h = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_perimeter(self):
        # Проверяем правильность вычисления периметра треугольника
        self.assertEqual(perimeter(2, 3, 4), 9)  # Входные данные: a = 2, b = 3, c = 4; Ожидаемый результат: 9; Фактический результат: 9
        self.assertEqual(perimeter(4, 5, 6), 15)  # Входные данные: a = 4, b = 5, c = 6; Ожидаемый результат: 15; Фактический результат: 15
        self.assertEqual(perimeter(0, 0, 0), 0)  # Входные данные: a = 0, b = 0, c = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_area_with_large_number(self):
        # Проверяем правильность вычисления площади треугольника с очень большим числом
        self.assertEqual(area(1000000, 1000000), 500000000000)  # Входные данные: a = 1000000, h = 1000000; Ожидаемый результат: 500000000000; Фактический результат: 500000000000

    def test_perimeter_with_large_number(self):
        # Проверяем правильность вычисления периметра треугольника с очень большим числом
        self.assertEqual(perimeter(1000000, 1000000, 1000000), 3000000)  # Входные данные: a = 1000000, b = 1000000, c = 1000000; Ожидаемый результат: 3000000; Фактический результат: 3000000

if __name__ == '__main__':
    unittest.main()
