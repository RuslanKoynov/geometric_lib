# General description:

**This project is a set of functions for calculating areas and perimeters of figures such as circle, rectangle, square and triangle. All of functions are written in Python language.**

---
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = 0.5(ah)

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
---
## Functions description.

### Circle's functions:

#### `area(r):`
##### Returns the area of a circle with an input value.
```python
from circle import area
r = float(input("Input radius of the circle: "))
print(f'Circle with radius {r} has area: {area(r)}')

Input radius of the circle: 4
Circle with radius 4.0 has area: 50.26548245743669
```

#### `perimeter(r):`
##### Returns the peremiter of a circle with an input value.
```python
from circle import perimeter
r = float(input("Input radius of the circle: "))
print(f'Circle with radius {r} has perimeter: {perimeter(r)}')

Input radius of the circle: 7
Circle with radius 7.0 has perimeter: 43.982297150257104
```

---

### Trinagle's functions:

#### `area(a, h):`
##### Returns the area of the triangle with an input value.

```python
from triangle import area
a = float(input("Input side of the triangle: "))
h = float(input("Input height of the triangle: "))
print(f'Triangle with side {a} and height {h} has area: {area(a, h)}')

Input side of the triangle: 5
Input height of the triangle: 7
Triangle with side 5.0 and height 7.0 has area: 17.5
```

#### `perimeter(a, h):`
##### Returns the perimeter of the triangle with an input value.

```python
from triangle import perimeter
a = float(input("Input first side of the triangle: "))
b = float(input("Input second side of the triangle: "))
c = float(input("Input third side of the triangle: "))
print(f'Triangle with first side {a}, second side {b} and third side {c} has perimeter: {perimeter(a, b, c)}')

Input first side of the triangle: 5
Input second side of the triangle: 6
Input third side of the triangle: 7
Triangle with first side 5.0, second side 6.0 and third side 7.0 has perimeter: 18.0
```

---

### Square's functions:

#### `area(a):`
##### Returns the area of the square with an input value.
```python
from square import area
a = float(input("Input side of the square: "))
print(f'Square with side {a} has area: {area(a)}')

Input side of the square: 6.5
Square with side 6.5 has area: 42.25
```

#### `perimeter(a):`
##### Returns the perimeter of the square with an input value.

```python
from square import perimeter
a = float(input("Input side of the square: "))
print(f'Square with side {a} has perimeter: {perimeter(a)}')

Input side of the square: 4.7
Square with side 4.7 has perimeter: 18.8
```

---

### Rectangle's functions:

#### `area(a, b):`
##### Returns the area of the square with an input value.

```python 
from rectangle import area
a = float(input("Input first side of the rectangle: "))
b = float(input("Input second side of the rectangle: "))
print(f'Rectangle with first side {a} and second side {b} has area: {area(a, b)}')

Input first side of the rectangle: 4
Input second side of the rectangle: 5
Rectangle with first side 4.0 and second side 5.0 has area: 20.0
```

#### `perimeter(a, b):`
##### Returns the perimeter of the square with an input value.

```python 
from rectangle import perimeter
a = float(input("Input first side of the rectangle: "))
b = float(input("Input second side of the rectangle: "))
print(f'Rectangle with first side {a} and second side {b} has perimeter: {perimeter(a, b)}')

Input first side of the rectangle: 4
Input second side of the rectangle: 5
Rectangle with first side 4.0 and second side 5.0 has perimeter: 18.0
```

---

## Git history:
|                   hash                   |           date           |   author  |                commit                |
|:----------------------------------------:|:------------------------:|:---------:|:------------------------------------:|
| d078c8d9ee6155f3cb0e577d28d337b791de28e2 | Thu Mar 4 14:55:29 2021  | smartiqa  | Docs added                           |
| ea95969922996038ff6e46b6b643cc4a14a7c10c | Wed Sep 20 23:42:15 2023 | Rostyslav | added file rectangle.py              |
| ed58a683200fe2b4243340f96c9e7e00facf0606 | Wed Sep 20 23:46:26 2023 | Rostyslav | fixed a bug in file rectangle.py     |
| 4f83c5b00507abfe3a8d739378b84e17534a3bc5 | Wed Oct 4 23:16:57 2023  | Rostyslav | comments were added to all functions |
