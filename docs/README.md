# Общее описание

Этот проект представляет собой набор модулей Python, которые реализуют функции для вычисления площадей и периметров различных геометрических фигур, таких как круг, прямоугольник, квадрат и треугольник. Каждый модуль содержит соответствующую функцию, которая принимает необходимые параметры и возвращает результат вычисления.

# Математические формулы
## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = (a  \*  h) / 2

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

# Описание функций с примерами вызовов

## Circle.py

- **area(r)** - Функция принимает один параметр: r - радиус круга. Возвращает значение площади круга, вычисленной как math.pi * r * r.

Пример кода на python

    import circle
    
    radius = 5
    area = circle.area(radius)
    print(area)  # Вывод: 78.5
    
    radius = 10
    area = circle.area(radius)
    print(area)  # Вывод: 314.2


- **perimeter(r)** - Функция принимает один параметр: r - радиус круга. Возвращает значение периметра круга, вычисленное как 2 * math.pi * r.

Пример кода на python

    import circle
    
    radius = 5
    perimeter = circle.perimeter(radius)
    print(perimeter)  # Вывод: 31.42
    
    radius = 10
    perimeter = circle.perimeter(radius)
    print(perimeter)  # Вывод: 62.83


## Rectangle.py

- **area(a, b)** -  Функция принимает два параметра: a - длина одной стороны прямоугольника, b - длина другой стороны прямоугольника. Возвращает значение площади прямоугольника, вычисленной по формуле a * b.

Пример кода на python

	import rectangle

    side_a = 5
    side_b = 10
    area = rectangle.area(side_a, side_b)
    print(area)  # Вывод: 50

    side_a = 15
    side_b = 20
    area = rectangle.area(side_a, side_b)
    print(area)  # Вывод: 300

- **perimeter(a, b)** - Функция принимает два параметра: a - длина одной стороны прямоугольника, b - длина другой стороны прямоугольника. Возвращает значение периметра прямоугольника, вычисленное как (a + b) * 2.

Пример кода на python
    
    import rectangle
    
    side_a = 5
    side_b = 10
    perimeter = rectangle.perimeter(side_a, side_b)
    print(perimeter)  # Вывод: 40
    
    side_a = 15
    side_b = 20
    perimeter = rectangle.perimeter(side_a, side_b)
    print(perimeter)  # Вывод: 90

## Square.py

- **area(side)** - Функция принимает один параметр: a - длина стороны квадрата.
    Возвращает значение площади квадрата, вычисленной по формуле a * a.

Пример кода на python

    import square
    
    side = 5
    area = square.area(side)
    print(area)  # Вывод: 25
    
    side = 10
    area = square.area(side)
    print(area)  # Вывод: 100

- **perimeter(a)** - Функция принимает один параметр: a - длина стороны квадрата.
    Возвращает значение периметра квадрата, вычисленное как 4 * a.

Пример кода на python

	import square
    
    side = 5
    perimeter = square.perimeter(side)
    print(perimeter)  # Вывод: 20
    
    side = 10
    perimeter = square.perimeter(side)
    print(perimeter)  # Вывод: 40

## Triangle.py

- **area(a, h)** - Функция принимает два параметра: a - длина основания треугольника, h - высота треугольника.Возвращает значение площади треугольника, вычисленной по формуле a * h / 2.

Пример кода на python

	import triangle
    
    base = 4
    height = 10
    area = triangle.area(base, height)
    print(area)  # Вывод: 7

- **perimeter(a, b, c)** - Функция принимает три параметра: a, b и c - длины сторон треугольника. Возвращает значение периметра треугольника, вычисленное как a + b + c.

Пример кода на python

    import triangle
    
    side_a = 4
    side_b = 8
    side_c = 6
    perimeter = triangle.perimeter(side_a, side_b, side_c)
    print(perimeter)  # Вывод: 18

# Изменения в проекте

| Хэш  | Автор | Дата  | Cообщение |
|:----------|:----------|:----------|:-----|
| 62d87ed29427d18fb1d942e477479d5f5808ba38    | Aleksevy <fusterune@icloud.com>   | Sun Dec 17 18:48:05 2023   |Add file rectangle.py                                |
| 391bc0c141bf88c68af5246490b70af88d4e4866    | Aleksevy <fusterune@icloud.com>   | Sun Dec 17 18:50:03 2023   |Fix: fixed error in rectangle.py                     | 
| 9ed9871f78b3c747b96a4c079fd5185bf9da2617    | Aleksevy <fusterune@icloud.com>   | Tue Dec 19 10:25:11 2023   |refactor: added a comment to the code in circle.py.  |
| 7300074e119d68cf5e20a6c521ad475e5c74218c    | Aleksevy <fusterune@icloud.com>   | Tue Dec 19 10:25:36 2023   |refactor: added a comment to the code in rectangle.py|
| bd2417dadf0cf4c6c94fb48b2db77652eab4e9f7    | Aleksevy <fusterune@icloud.com>   | Tue Dec 19 10:25:56 2023   |refactor: added a comment to the code in square.py.  |
| 16f309f0b2cf1c16529ed021fb6151d6d06220c1    | Aleksevy <fusterune@icloud.com>   | Tue Dec 19 10:26:15 2023   |refactor: added a comment to the code in triangle.py.|
