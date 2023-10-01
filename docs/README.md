# documentation

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

## general description of the solution
In general, the solution consists of two stages:
1. The function receives a certain number(s), which are the length of some elements of the figure.
2. Mathematical operations are performed with the given number(s), with the help of which the area or volume of the figure is calculated (depending on the formulas).
3. The program returns the result.

## functions

> Programming language - Python.

### Ciecle

*** Program: ***

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

*** Example of a call: ***

```python
r = 3
print("Area = ", area(r))
print("Perimeter = ", perimeter(r))
```
output:
Area = 28,27433
Perimeter = 18,84956

## Rectangle

*** Program: ***

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

*** Example of a call: ***

```python
a = 5
b = 6
print("Area = ", area(a, b))
print("Perimeter = ", perimeter(a, b))
```

output:
Area = 30
Perimeter = 22

## Square

*** Program: ***

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

*** Example of a call: ***

```python
a = 5
print("Area = ", area(a))
print("Perimeter = ", perimeter(a))
```

output:
Area = 25
Perimeter = 20

## Triangle

*** Program: ***

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

*** Example of a call: ***

```python
a = 3
b = 4
c = 5
h = 4
print("Area = ", area(a, h))
print("Perimeter = ", perimeter(a, b, c))
```

output:
Area = 6
Perimeter = 12