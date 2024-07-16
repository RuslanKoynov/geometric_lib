import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

# Тест 1: Проверка площади и периметра квадрата с положительной стороной
a = 2
expected_area = a * a
expected_perimeter = 4 * a
actual_area = area(a)
actual_perimeter = perimeter(a)
print(f"Тест 1: a = {a}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 2: Проверка площади и периметра квадрата с отрицательной стороной
a = -3
expected_area = a * a
expected_perimeter = 4 * a
actual_area = area(a)
actual_perimeter = perimeter(a)
print(f"Тест 2: a = {a}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

# Тест 3: Проверка площади и периметра квадрата с нулевой стороной
a = 0
expected_area = a * a
expected_perimeter = 4 * a
actual_area = area(a)
actual_perimeter = perimeter(a)
print(f"Тест 3: a = {a}")
print(f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {actual_area}")
print(f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {actual_perimeter}")
print()

class SquareTests(unittest.TestCase):
    def test_area(self):
        # Проверяем правильность вычисления площади квадрата
        self.assertEqual(area(2), 4)  # Входные данные: a = 2; Ожидаемый результат: 4; Фактический результат: 4
        self.assertEqual(area(4), 16)  # Входные данные: a = 4; Ожидаемый результат: 16; Фактический результат: 16
        self.assertEqual(area(0), 0)  # Входные данные: a = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_perimeter(self):
        # Проверяем правильность вычисления периметра квадрата
        self.assertEqual(perimeter(2), 8)  # Входные данные: a = 2; Ожидаемый результат: 8; Фактический результат: 8
        self.assertEqual(perimeter(4), 16)  # Входные данные: a = 4; Ожидаемый результат: 16; Фактический результат: 16
        self.assertEqual(perimeter(0), 0)  # Входные данные: a = 0; Ожидаемый результат: 0; Фактический результат: 0

    def test_area_with_large_number(self):
        # Проверяем правильность вычисления площади квадрата с очень большим числом
        self.assertEqual(area(1000000), 1000000000000)  # Входные данные: a = 1000000; Ожидаемый результат: 1000000000000; Фактический результат: 1000000000000

    def test_perimeter_with_large_number(self):
        # Проверяем правильность вычисления периметра квадрата с очень большим числом
        self.assertEqual(perimeter(1000000), 4000000)  # Входные данные: a = 1000000; Ожидаемый результат: 4000000; Фактический результат: 4000000

if __name__ == '__main__':
    unittest.main()
