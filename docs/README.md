# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
  
# Описание проекта

Этот проект представляет собой набор функций для вычисления площади и периметра геометрических фигур. Включает функции для работы с треугольниками и прямоугольником.

## Использование

Для использования функций проекта, вы можете импортировать соответствующие модули и вызвать соответствующие функции.

Пример использования:

# python
from triangle import area, perimeter

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

# Вычисление площади и периметра треугольника
triangle_area = area(5, 8)

triangle_perimeter = perimeter(3, 4, 5)

# Вычисление площади и периметра квадрата
rectangle_side_A = 6

rectangle_side_B = 8

rectangle_area_result = rectangle_area(square_side_A, square_side_B)

rectangle_perimeter_result = rectangle_perimeter(square_side)
