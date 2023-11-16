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
print("error")

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

class RectangleTests(unittest.TestCase):
    def test_area(self):
        # Проверяем правильность вычисления площади прямоугольника
        self.assertEqual(area(2, 3), 6)  # Входные данные: a = 2, b = 3; Ожидаемый результат: 6; Фактический результат: 6
        self.assertEqual(area(4, 5), 20)  # Входные данные: a = 4, b = 5; Ожидаемый результат: 20; Фактический результат: 20
        self.assertEqual(area(0, 0), 0)  # Входные данные: a = 0, b = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_perimeter(self):
        # Проверяем правильность вычисления периметра прямоугольника
        self.assertEqual(perimeter(2, 3), 10)  # Входные данные: a = 2, b = 3; Ожидаемый результат: 10; Фактический результат: 10
        self.assertEqual(perimeter(4, 5), 18)  # Входные данные: a = 4, b = 5; Ожидаемый результат: 18; Фактический результат: 18
        self.assertEqual(perimeter(0, 0), 0)  # Входные данные: a = 0, b = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_area_with_large_number(self):
        # Проверяем правильность вычисления площади прямоугольника с большими числами
        self.assertEqual(area(1000000, 1000000), 1000000000000)  # Входные данные: a = 1000000, b = 1000000; Ожидаемый результат: 1000000000000; Фактический результат: 1000000000000

    def test_perimeter_with_error(self):
        # Проверяем правильность вычисления периметра прямоугольника с ошибкой
        self.assertEqual(perimeter(3, 4), 14)  # Входные данные: a = 3, b = 4; Ожидаемый результат: 14; Фактический результат: 14

if __name__ == '__main__':
    unittest.main()