# Geometric lib
## General description of the solution
Geometric lib - is a library of programs with which you can calculate the perimeters and areas of various shapes.

# Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
# Programs
## circle.py
```python
import math
'''
Модуль math предоствляет обширный функционал для проведения вычислений 
с вещественными числами(числами с плавающей точкой).
'''
def area(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает площадь круга, вычисляя ее по формуле: π * r^2
    '''
    return math.pi * r * r
def perimeter(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: 2 * π * r
    '''
    return 2 * math.pi * r
```
### Example
```python
r = 2
print (f"Area = area(r)); Perimetr = {perimetr(r)}")
```
```
Area = 12.566370614359172; Perimeter = 12.566370614359172
```
## rectangle.py
```python
def area(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает площадь прямоугольника, вычисляя ее по формуле: a * b
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает периметр прямоугольника, вычисляя его по формуле: 2 * (a + b)
    '''
    return 2 * (a + b)
```
### Example
```python
a = 3
b = 5
print (f"Area = fare(a, b)}; Perimetr = {perimetr(a, b)}")
```
```
Area = 15; Perimetr = 16
```
## square.py
```python
def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает площадь квадрата, вычисляя ее по формуле: a^2
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает периметр квадрата, вычисляя его по формуле: 4 * a
    '''
    return 4 * a
```
### Example
```python
a = 2
print (f"Area = {area(a)}; Perimetr = {perimetr(a)}")
```
```
Area = 4; Perimetr = 8
```
## triangle.py
```python
def area(a, h):
    '''
    Принимает два числа, одно из них является стороной треугольника, другое его высотой: a, h
    Возвращает площадь треугольника, вычисляя ее по формуле: (a * h) / 2
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
    Принимает три числа, которые являются сторонами треугольника: a, b, c
    Возвращает периметр треугольника, вычисляя его по формуле: a + b + c
    '''
    return a + b + c
```
### Example
```python
a = 3
b = 4
с = 5
h = 2
print (f"Area = {area(a, h)}; Perimetr = {perimetr(a, b, c)}")
```
```
Area = 3; Perimetr = 12
```
## Commit History
```
commit 02cb7271e3ccda989bd04b98e01fa00ecf276c60 (HEAD -> lab2)
Author: monak23 <monak.v@yandex.ru>
Date:   Wed Oct 4 14:19:26 2023 +0300

    File Declaration

commit 6691589d2c37004c5e7eb598a8e5654527be9141 (origin/main, origin/HEAD, main)
Author: monak23 <monak.v@yandex.ru>
Date:   Wed Sep 20 10:32:44 2023 +0300

    file fixed

commit 0aa178a59f6937f3464c3ce27ef6dc289b0d0d34
Author: monak23 <monak.v@yandex.ru>
Date:   Wed Sep 20 10:30:16 2023 +0300

    file rectangle.py added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300
```
