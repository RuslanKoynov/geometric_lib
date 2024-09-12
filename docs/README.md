# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
# Description
- Created functions to find areas and perimeters of listed shapes: _circle, triangle, rectangle, square_
# Description of functions
## Circle
```python
import math
    #Import library math for pi value#
def area(r):
    #Accepts radius of circle r and returns the area of circle#
    if (type(r) == str or r < 0):
        return False
    return math.pi * r * r
def perimeter(r):
    #Accepts radius of circle r and returns the perimeter of circle#
    if (type(r) == str or r < 0):
        return False
    return 2 * math.pi * r
```
### Example of calling Circle:
```python
print(area(10))
print(perimeter(3))

```
- Result area(10): 314.1592653589793
- Result perimeter(3): 18.84955592153876

## Triangle
```python
def area(a, h):
    #Accepts side and height of triangle a, h
    #and returns the area of triangle#
    if (type(a) == str or type(h) == str or a < 0 or h < 0):
        return False
    return (a * h) / 2 
def perimeter(a, b, c):
    #Accepts sides of triangle a,b,c
    #and returns the perimeter of triangle#
    if (type(a) == str or type(b) == str or type(c) == str or \
        a < 0 or b < 0 or c < 0):
        return False
    return a + b + c
```
### Example of calling Triangle
```python
print(area(10, 5))
print(perimeter(3, 4, 5))
```
- Result area(10, 5): 25.0
- Result perimeter(3, 4, 5): 12

## Rectangle
```python
def area(a, b):
    #Accepts sides of rectangle a,b and returns the area of rectangle#
    if (type(a) == str or type(b) == str or a < 0 or b < 0):
        return False
    return a * b 
def perimeter(a, b):
    #Accepts sides of rectangle a,b and returns the perimeter of rectangle#
    if (type(a) == str or type(b) == str or a < 0 or b < 0):
        return False
    return 2*(a + b)
```
### Example of calling Rectangle
```python
print(area(2, 3))
print(perimeter(2, 3))
```
- Result area(2, 3): 6
- Result perimeter(2, 3): 10

## Square
```python
def area(a):
    #Accepts side of square a and returns the area of square#
    if (type(a) == str or a < 0):
        return False
    return a * a
def perimeter(a):
    #Accepts side of square a and returns the perimeter of square#
    if (type(a) == str or a < 0):
        return False
    return 4 * a
```
### Example of calling Square

```python
print(area(4))
print(perimeter(5))
```
- Result area(4): 16
- Result perimeter(5): 20

# Project history with commit hashes
> __commit 6bdb310472a32ebe476298cd31e2ea04f2de6e2b (origin/new_features_408789, new_features_408789)__
> - Author: Alina <408789@niuitmo.ru>
> - Date:   Sun Sep 17 14:39:11 2023 +0300
> 
- Была исправлена ошибка в файле rectangle.py

> __commit 371e693ba0fc9c4268009c31f3a1849ddb672253__
> - Author: Alina <408789@niuitmo.ru>
> - Date:   Sun Sep 17 12:49:43 2023 +0300
>
- Добавлен новый файл rectangle.py

> __commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)__
> - Author: smartiqa <info@smartiqa.ru>
> - Date:   Thu Mar 4 14:55:29 2021 +0300
>
- L-03: Docs added

> __commit 8ba9aeb3cea847b63a91ac378a2a6db758682460__
> - Author: smartiqa <info@smartiqa.ru>
> - Date:   Thu Mar 4 14:54:08 2021 +0300
>
- L-03: Circle and square added

# Unittest

|Function       | Values   | Expected | Test result |
| :-----------: |:--------:|:----:|:----:|
| Circle.py     | r = 0    |area = 0|area = 0|
| Circle.py     | r = 11  |perimeter = 69.11503837897544|perimeter = 69.11503837897544|
| Rectangle.py  | a = 33, b = 33|area = 1089|area = 1089|
| Rectangle.py  | a = -100, b = 23|perimeter expected False, because this case is considered in the funcion|perimeter = False|
| Square.py     | a = 0.03    |area = 0.0009|area = 0.0009|
| Square.py     | a = 0    |perimeter = 0|perimeter = 0|
| Triangle.py   | a = 123, h = 54    |area = 3321|area = 3321|
| Triangle.py   | a = 'goingstrong', b = 70, c = 'still' |perimeter expected False, because this case is considered in the funcion|perimeter = False|







