# geometric_lib
**geometric_lib** contains various useful functions for calculating geometric shapes.

## Features
**geometric_lib** allows you to work with the following geometric shapes
- [Circle](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2#circle.py)
- [Rectangle](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2#rectangle)
- [Square](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2#square)
- [Triangle](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2#triangle)


### Circle
[Code](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2/circle.py)
```python
import math


def area(r):
	'Calculates the area of circle'
    return math.pi * r * r

```
Input: 3

Output: 28.274333882308138


```python
def perimeter(r):
	'Calculates the perimeter of circle'
    return 2 * math.pi * r
```
Input: 3

Output: 18.84955592153876


### Rectangle
[Code](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2/rectangle.py)
```python
def area(a, b):
	'Calculates the area of rectangle'
    return a * b
```
Input: 3 4 

Output: 12


```python
def perimeter(a, b):
    'Calculates the perimeter of rectangle'
    return 2 * (a + b)
```
Input: 1 2

Output: 6


### Square
[Code](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2/square.py)
```python
def area(a):
    'Calculates the area of a square'
    return a * a
```
Input: 6

Output: 36


```python
def perimeter(a):
    'Calculates the perimeter of a square'
    return 4 * a
```
Input: 4

Output: 16


### Triangle
[Code](https://github.com/bemooooooooo/geometric_lib/blob/gitlab2/triangle.py)

```python
def area(a, h):
    'Calculates the area of triangle'
    return a * h / 2
```
Input: 5 2

Output: 5


```python
def perimeter(a, b, c):
    'Calculates the perimeter of triangle'
    return a + b + c
```
Input: 3 4 5

Output: 12


## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2


### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c


Project change history with commit hashes:


| Hash  | Commit | Branch |
| ---------| ------------------------------------------- | ------------------------------- |
| d3aa15   | added documentation for triangle.py         | (HEAD -> gitlab2)               |
| 63fb83   | added documentation for square.py           | -                               |
| dc69d3   | added documentation for rectangle.py        | -                               |
| 5e071d   | added documentation for circle.py           | -                               |
| ac2c59   | fixed function perimeter in rectangle.py    | (origin/main, origin/HEAD, main)|
| 261ec4   | add triangle.py                             | -                               |
| e5bae3   | add rectangle.py                            | -                               |
| d078c8   | Docs added                                  | L-03                            |
| 8ba9ae   | Circle and square added                     | L-03                            |

