# Документация
## Математические формулы
### Площадь
- Окружность: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = (a * h) / 2

### Периметр
- Окружность: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

## Общее описание решения
На вход каждой функции подаются аргументы - параметры соответсвующих фигур. 
Каждая функция возвращает результат выполнения формулы к параметрам.

## Описание каждой функции с примерами вызова
### square
```python
def area(a):
    return a * a


def perimeter(a):
    return 4 * a
```

***Описание аргументов функции:***\
*a(float)*: сторона квадрата

***Пример вызова:***\
area(10) = 100\
perimeter(10) = 40

### circle
```python
import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r
```

***Описание аргументов функции:***\
*r(float)*: радиус окружности

***Пример вызова:***\
area(1) = 3.141592653589793\
perimeter(1) = 6.283185307179586

### rectangle
```python
def area(a, b):
    return a * b


def perimeter(a, b):
    return 2 * (a + b)

```

***Описание аргументов функции:***\
*a(float)*: первая сторона прямоугольника\
*b(float)*: вторая сторона прямоугольника

***Пример вызова:***\
area(5, 10) = 50\
perimeter(5, 10) = 30

### triangle
```python
def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c
```

***Описание аргументов функции:***\
*a(float)*: сторона треугольника\
*h(float)*: прилегающая к ней высота

***Пример вызова:***\
area(5, 10) = 25\
perimeter(5, 10, 25) = 40

## История изменения проекта с хешами коммитов
```markdown
939f844: "docs: functions declaration comments in triangle.py"
d80341d: "docs: functions declaration comments in rectangle.py"
f128eff: "docs: functions declaration comments in circle.py"
47520fb: "docs: functions declaration comments in square.py"
5c115f6: "fix: rectangle's perimeter feature"
4af2b5b: "feat: add triangle features"
d7a4894: "feat: add rectangle features"
d078c8d: "L-03: Docs added"
8ba9aeb: "L-03: Circle and square added"
```