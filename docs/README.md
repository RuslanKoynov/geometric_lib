# Общее описание решения
Этот проект создан для того, чтобы считать площади и периметра кругов, квадратов, прямоугольников и треугольников

# Описание каждой функции с примерами вызова 
## Прямоугольник
### Площадь
Функция площади прямоугольника возвращает площадь прямоугольника по заданным сторонам
```py
rectangle_area = area(10, 20)
rectangle_area = 200
```
### Периметр

Функция периметра прямоугольника возвращает периметр прямоугольника по заданным сторонам
```py
rectangle_perimetr = perimetr(10, 20)
rectangle_perimetr = 60
```
## Треугольник
### Площадь
Функция площади треугольника возвращает площадь треугольника по заданным основанию и высоте
```py
triangle_area = area(10, 20)
triangle_area = 100
```

### Периметр
Функция периметра треугольника возвращает периметр треугольника по заданным сторонам
```py
triangle_perimetr = perimetr(10, 20, 30)
triangle_perimetr = 60
```
## Квадрат
### Площадь
Функция площади квадрата возвращает площадь квадрата по заданной стороне
```py
square_area = area(10)
square_area = 100
```
### Периметр

Функция периметра квадрата возвращает периметр квадрата по заданной стороне
```py
square_perimetr = perimetr(10)
square_perimetr = 40
```
## Круг
### Площадь
Функция площади круга возвращает площадь круга по заданному радиусу
```py
circle_area = area(10)
circle_area = 314
```
### Периметр

Функция периметра круга возвращает периметр круга по заданному радиусу
```py
circle_perimetr = perimetr(10)
circle_perimetr = 62,8
```

# Тесты
| Тип теста               | Значение 1 | Значение 2 | Значение 3 | Результат |
|-------------------------|------------|------------|------------|-------|
| Площадь прямоугольника  | 10         | 0          | -          | 0     |
| Площадь прямоугольника  | 10         | 10         | -          | 100   |
| Периметр прямоугольника | 0          | 0          | -          | 0     |
| Периметр прямоугольника | 10         | 10         | -          | 40    |
| Площадь треугольника    | 10         | 0          | -          | 0     |
| Площадь треугольника    | 10         | 10         | -          | 50    |
| Периметр треугольника   | 0          | 0          | 0          | 0     |
| Периметр треугольника   | 10         | 10         | 10         | 30    |
| Площадь квадрата        | 0          | -          | -          | 0     |
| Площадь квадрата        | 10         | -          | -          | 100   |
| Периметр квадрата       | 0          | -          | -          | 0     |
| Периметр квадрата       | 10         | -          | -          | 40    |
| Площадь круга           | 0          | -          | -          | 0     |
| Площадь круга           | 10         | -          | -          | 100 * π |
| Периметр круга          | 0          | -          | -          | 0     |
| Периметр круга          | 10         | -          | -          | 20 * π |

## Тесты для подсчёта площади и периметра прямоугольника
```py
class RectangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
```
## Тесты для подсчёта площади и периметра треугольника
```py
class TriangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0, 0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
```
## Тесты для подсчёта площади и периметра квадрата
```py
class SquareTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_mul_perimeter(self):
        res = perimeter (0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
```
## Тесты для подсчёта площади и периметра круга
```py
class CircleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_zero_mul_perimeter(self):
        res = perimeter (0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)
```
# История изменения проекта с хэшами комитов
- изменение от 10 сентября 2023 18:08 '''hash: 96352e5''' - добавлены формулы для прямоугольника
- изменение от 10 сентября 2023 18:11 '''hash: f7a72ce''' - правка формул для прямоугольника
