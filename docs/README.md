# Документация

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (ah)/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Общее описание решения
1. Функция принимает какое-то значение.
2. Производятся математические операции над значением.
3. Функция выдает результат.

## Описание каждой функции с примерами вызова

### Круг

***Программа:***

```python
import math
'''Модуль math предоставляет обширный функционал для работы с числами'''

def area(r):
    '''Поступает число r-радиус круга. Функция возвращает число Pi умноженное на r в квадрате (площадь круга)'''
    return math.pi * r * r


def perimeter(r):
    '''Поступает число r-радиус круга. Функция возвращает число 2 умноженное на число Pi умноженное на r (периметр круга)'''
    return 2 * math.pi * r
```

***Пример вызова:***

*Input:* r = 7

*Output:* Площадь = 153.938040, Периметр = 43.982297

### Прямоугольник

***Программа:***

```python
def area(a, b):
    '''Поступают числа a и b-стороны прямоугольника.Функция возвращает число a умноженное на число b (площадь прямоугольника)'''
    return a * b


def perimeter(a, b):
    '''Поступают числа a и b-стороны прямоугольника.Функция возвращает удвоенную сумму чисел a и b (периметр прямоугольника)'''
    return 2*(a+b)
```

***Пример вызова:***

*Input:* a = 2, b = 5

*Output:* Площадь = 10, Периметр = 14

### Квадрат

```python
def area(a):
    '''Поступает число a-сторона квадрата. Функция возвращает число a в квадрате (площадь квадрата)'''
    return a * a


def perimeter(a):
    '''Поступает число a-сторона квадрата. Функция возвращает число a умноженное на число 4 (периметр квадрата)'''
    return 4 * a
```

***Пример вызова:***

*Input:* a = 6

*Output:* Площадь = 36, Периметр = 24

### Треугольник

```python
def area(a, h):
    '''Поступают числа a и h-сторона и высота треугольника.Функция возвращает произведение a и h деленное на 2 (площадь треугольника)'''
    return a * h / 2


def perimeter(a, b, c):
    '''Поступают числа a,b,c-стороны треугольника. Функция возвращает сумму a,b,c (периметр треугольника)'''
    return a + b + c
```

***Пример вызова:***

*Input:* a = 5, h = 10, b = 7, c = 2

*Output:* Площадь = 25.0, Периметр = 14

## История изменения проекта с хешами комитов (кроме последней записи)

commit 7b86dcbb9bdba8e1cb0c05b9904cd5cd36695d54
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 01:20:24 2023 +0300

    added general description of the solution to README.md

commit fed0a4a623a6b30d31b2594aac21108f888a5930
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:31:52 2023 +0300

    added documentation to triangle.py

commit a33eec879c9b2d0a78b55a3ccc126dac8e1db66d
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:30:01 2023 +0300

    added documentation to square.py
:...skipping...
commit ef7ea08ac323522940acb32b9a37fbb7a4026182 (HEAD -> documentation_413823)
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 23:26:03 2023 +0300

    added description of each function with call examples

commit 7b86dcbb9bdba8e1cb0c05b9904cd5cd36695d54
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 01:20:24 2023 +0300

    added general description of the solution to README.md

commit fed0a4a623a6b30d31b2594aac21108f888a5930
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:31:52 2023 +0300

    added documentation to triangle.py

commit a33eec879c9b2d0a78b55a3ccc126dac8e1db66d
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:30:01 2023 +0300

    added documentation to square.py

commit 5e848031cf1b99854b954c7dcaa4f4f183bd3dad
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:26:39 2023 +0300

    added documentation to rectangle.py

commit bd06a2805d9fc59732a5973dbc33df2703c01ad9
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Wed Oct 4 00:25:16 2023 +0300

    added documentation to circle.py

commit d8fd8e6dd2f18cc968a670af5fa0a9e747bd95bb (origin/main, origin/HEAD, main)
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Mon Sep 18 05:30:55 2023 +0300

    added all changes

commit 199a4c067496f2e847db6c022f327e95941569ed
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Mon Sep 18 05:23:24 2023 +0300

    fixed a mistake in rectangle.py

commit a884e3247c95a98a53564ca19893302ae2fd4e62
Author: Adriana Khudoba <adriana0kot@gmail.com>
Date:   Mon Sep 18 05:20:16 2023 +0300

    added a new file rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added