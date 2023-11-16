# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

Использование

Для использования функций проекта, вы можете импортировать соответствующие модули и вызвать соответствующие функции.

Пример использования:

python

from triangle import area, perimeter

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

Вычисление площади и периметра треугольника

triangle_area = area(5, 8)

triangle_perimeter = perimeter(3, 4, 5)

Вычисление площади и периметра квадрата

rectangle_side_A = 6

rectangle_side_B = 8

rectangle_area_result = rectangle_area(square_side_A, square_side_B)

rectangle_perimeter_result = rectangle_perimeter(square_side)

##CIRCLE
import unittest
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


##TRIANGLE
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


##SQUARE
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



  ##RECTANGLE
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


