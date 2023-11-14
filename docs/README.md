# Documentation

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

## General description of the solution
In general, the solution consists of three stages:
1. The function receives a certain number(s), which are the length of some elements of the figure.
2. Mathematical operations are performed with the given number(s), with the help of which the area or volume of the figure is calculated (depending on the formulas).
3. The program returns the result.

## Functions

> Programming language - Python.

### Ciecle

***Program:***

```python
import math

'''Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.'''

def area(r):
   
    '''Принимает  число r - радиус круга.
    Возвращает r в квадрате умноженное на число Pi, т.е. площадь круга.'''

    return math.pi * r * r

def perimeter(r):
    
     '''Принимает число r - радиус круга.
    Возращает удвоенное произведение числа r на pi, т.е. пириметр круга.'''
    
    return 2 * math.pi * r
```

***Example of a call:***

```python
r = 3
print("Area = ", area(r))
print("Perimeter = ", perimeter(r))
```

```markdown
output:
Area = 28,27433
Perimeter = 18,84956
```

## Rectangle

***Program:***

```python
 def area(a, b):

    '''Принимает числа a и b - стороны прямоугольника.
    Возращает произведение a и b, т.е. площадь прямоугольника.'''

    return a * b 
    
def perimeter(a, b): 

    '''Принимает числа a и b - стороны прямоугольника.
    Возращет удвоенную сумму a и b, т.е. пириметр прямоугльника.'''
    
    return 2 * (a + b) 
```

***Example of a call:***

```python
a = 5
b = 6
print("Area = ", area(a, b))
print("Perimeter = ", perimeter(a, b))
```

```markdown
output:
Area = 30
Perimeter = 22
```

## Square

***Program:***

```python
def area(a):

    '''Принимает число a - сторону квадрата.
    Возращает a в квадрате, т.е. площадь квадрата.'''

    return a * a

def perimeter(a):

    '''Принимает число a - сторону квадрата.
    Возращает a умноженное на 4, т.е. пириметр квадрата.'''
    
    return 4 * a
```

***Example of a call:***

```python
a = 5
print("Area = ", area(a))
print("Perimeter = ", perimeter(a))
```

```markdown
output:
Area = 25
Perimeter = 20
```

## Triangle

***Program:***

```python
def area(a, h): 

    '''Принимает числа a и h - сторону и высоту треугольника.
    Возращает произведение a и h деленное на 2, т.е. площадь треугольника.'''

    return a * h / 2 

def perimeter(a, b, c): 

    '''Принимает числа a, b и c - стороны треугольника.
    Возращает сумму a, b и c, т.е. пириметр треугольника.'''

    return a + b + c
```

***Example of a call:***

```python
a = 3
b = 4
c = 5
h = 4
print("Area = ", area(a, h))
print("Perimeter = ", perimeter(a, b, c))
```

```markdown
output:
Area = 6
Perimeter = 12
```

## Tests

Tests for testing area and perimeter functions have appeared:
1. test_circle.py - circle test suite
2. test_rectangle.py - rectangle test suite
3. test_square.py - square test suite
4. test_triangle.py - triangle test suite

Total tests - 49

Correct tests - 38

Incorrect tests - 11

Percentage of correct tests - 77%


## Commit history

commit 9cb3b42612c74299294dfc48972ed7374cfd2ba4 (HEAD -> tests_409950)
Author: Yandolav <yandolav@mail.ru>
Date:   Tue Nov 14 22:17:17 2023 +0300

    test: added new tests for all functions

commit fe1db763c3d0b09bf8adcb95e30c301a84150e9f
Author: Yandolav <yandolav@mail.ru>
Date:   Tue Nov 14 17:41:32 2023 +0300

    test: Added tests for triangle, circle, square and rectangle

commit e3c4ce1594b59f1771ef7963d677f64424f9f841 (documentation_409950)
Author: Yandolav <yandolav@mail.ru>
Date:   Tue Nov 14 16:51:14 2023 +0300

    style: switched to pancharm and adjusted the functions

commit 537eaaeef88c0cf240f0175d7c857924349acdca (HEAD -> documentation_409950)
Author: Yandolav <yandolav@mail.ru>
Date:   Sun Oct 1 14:19:55 2023 +0300

    docs: Added a section with commit history

commit 36a6e9282fa6a647badd316bf4601be432e70cfd (HEAD -> documentation_409950)
Author: Yandolav <yandolav@mail.ru>
Date:   Sun Oct 1 14:01:49 2023 +0300

    docs: Added a section related to functions

commit 92633a073463eda446df0e6cb4553a8abaa69ee0
Author: Yandolav <yandolav@mail.ru>
Date:   Fri Sep 29 17:19:51 2023 +0300

    docs: added a triangle to mathematical formulas

commit 7d44d7da214edf824bd1fd1e3d258cd77553b6a5
Author: Yandolav <yandolav@mail.ru>
Date:   Fri Sep 29 17:10:47 2023 +0300

    docs: added a general description of the solution

commit 3353dd09c85a9659492dfc0fe94454b7bc3d5d62
Author: Yandolav <yandolav@mail.ru>
Date:   Fri Sep 29 12:25:58 2023 +0300

    docs: added a description of the functions

commit e3530b2b5cd74404efe1070bfe652d768ff9dae1 (origin/new_features_409950, origin/main, origin/HEAD, main)
Author: Yandolav <yandolav@mail.ru>
Date:   Sat Sep 16 19:34:21 2023 +0300

    bug fixed

commit e918e86195f021c59eefff53dc3ee6c83a338d64
Author: Yandolav <yandolav@mail.ru>
Date:   Sat Sep 16 19:29:40 2023 +0300

    new file 2

commit 1c4614c4c7d1d0a6bb97d290f41d44121403ad53
Author: Yandolav <yandolav@mail.ru>
Date:   Sat Sep 16 19:26:58 2023 +0300

    new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
