
# Описание проекта

Данный проект представляет собой набор модулей Python, которые реализуют функции для вычисления площадей и периметров геометрических фигур таких как: круг, прямоугольник, квадрат и треугольник. Каждый модуль содержит соответствующую функцию, которая принимает необходимые параметры и возвращает результат вычисления.

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

- _**area(r)**_ - Функция принимает один параметр: r - радиус круга. Возвращает значение площади круга, вычисленной как math.pi * r * r.

Пример кода на python

```python
    import circle

    radius = 10
    area = circle.area(radius)
    print(area)  # Вывод: 314.2

    radius = 15
    area = circle.area(radius)
    print(area)  # Вывод: 706.9
```    


- _**perimeter(r)**_ - Функция принимает один параметр: r - радиус круга. Возвращает значение периметра круга, вычисленное как 2 * math.pi * r.

Пример кода на python
```python
    import circle

    radius = 10
    perimeter = circle.perimeter(radius)
    print(perimeter)  # Вывод: 62.83

    radius = 15
    perimeter = circle.perimeter(radius)
    print(perimeter)  # Вывод: 94.25

```

## Rectangle.py

- _**area(a, b)**_ -  Функция принимает два параметра: a - длина одной стороны прямоугольника, b - длина другой стороны прямоугольника. Возвращает значение площади прямоугольника, вычисленной по формуле a * b.

Пример кода на python
```python
	import rectangle

    side_a = 10
    side_b = 15
    area = rectangle.area(side_a, side_b)
    print(area)  # Вывод: 150

    side_a = 20
    side_b = 25
    area = rectangle.area(side_a, side_b)
    print(area)  # Вывод: 500
```

- _**perimeter(a, b)**_ - Функция принимает два параметра: a - длина одной стороны прямоугольника, b - длина другой стороны прямоугольника. Возвращает значение периметра прямоугольника, вычисленное как (a + b) * 2.


Пример кода на python
```python
    import rectangle

    side_a = 10
    side_b = 15
    perimeter = rectangle.perimeter(side_a, side_b)
    print(perimeter)  # Вывод: 50

    side_a = 20
    side_b = 25
    perimeter = rectangle.perimeter(side_a, side_b)
    print(perimeter)  # Вывод: 90
```

## Square.py

- _**area(side)**_ - Функция принимает один параметр: a - длина стороны квадрата.
    Возвращает значение площади квадрата, вычисленной по формуле a * a.

Пример кода на python
```python
    import square

    side = 10
    area = square.area(side)
    print(area)  # Вывод: 100

    side = 20
    area = square.area(side)
    print(area)  # Вывод: 400
```
- _**perimeter(a)**_ - Функция принимает один параметр: a - длина стороны квадрата.
    Возвращает значение периметра квадрата, вычисленное как 4 * a.

Пример кода на python
```python
    import square

    side = 10
    perimeter = square.perimeter(side)
    print(perimeter)  # Вывод: 40

    side = 20
    perimeter = square.perimeter(side)
    print(perimeter)  # Вывод: 80
```
## Triangle.py

- _**area(a, h)**_ - Функция принимает два параметра: a - длина основания треугольника, h - высота треугольника.Возвращает значение площади треугольника, вычисленной по формуле a * h / 2.

Пример кода на python
```python
    import triangle

    base = 20
    height = 12
    area = triangle.area(base, height)
    print(area)  # Вывод: 120
```

- _**perimeter(a, b, c)**_ - Функция принимает три параметра: a, b и c - длины сторон треугольника. Возвращает значение периметра треугольника, вычисленное как a + b + c.

Пример кода на python
```python
    import triangle

    side_a = 10
    side_b = 18
    side_c = 16
    perimeter = triangle.perimeter(side_a, side_b, side_c)
    print(perimeter)  # Вывод: 44
```


# Изменения в проекте

| Хэш                                      | Автор                             | Дата                              | Cообщение                           |
|:-----------------------------------------|:----------------------------------|:----------------------------------|:------------------------------------|
| c91550ad483401039dd560cc1a0d768fc2d2bb6f | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 05:56:41 2023 +0300    | commit                              |
| d830920efd28133680ee326aba76338631fd3e96 | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 05:04:12 2023 +0300    | Исправлена ошибка файла треугольник | 
| aa30280d5e0a152102500630add68bb807b675e2 | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 04:54:10 2023 +0300    | Добавлен файл треугольник           |
| 66e18ded95125e66c7e7be3785ff4dc201881157 | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 04:44:04 2023 +0300    | Добавлен файл прямоугольник         |
| 5fafde740713b5d7b7bf4fa07ff02034c17bbd94 | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 03:50:58 2023 +0300    | Прямоугольник модиф                 |
| 8bfc9b1422e2c1f9ef6b39999c5f128d3425dd13 | v1vid <shunyaevv23@gmail.com>     | Thu Dec 21 03:41:56 2023 +0300    | Прямоугольник                       |
| d078c8d9ee6155f3cb0e577d28d337b791de28e2 | smartiqa <info@smartiqa.ru>       | Thu Mar 4 14:55:29 2021 +0300     | Docs added                          |
| 8ba9aeb3cea847b63a91ac378a2a6db758682460 | smartiqa <info@smartiqa.ru>       | Thu Mar 4 14:54:08 2021 +0300     | Circle and square added             |
                                     
=======

