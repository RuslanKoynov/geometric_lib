# Documentation
This documentation for geometric_lib in python.
## Math formulas
| Shape     | Ares            | Perimeter                 |
|-----------|-----------------|---------------------------|
| Circle    | S = πR²         | P = 2πR                   |
| Rectangle | S = ab          | P = 2a + 2b               |
| Square    | S = a²          | P = 4a                    |
| Triangle  | S = a/h         | P = a + b + c             |


## circle.py

**General Description**

The `circle.py` module provides two functions for calculating the area and perimeter of a circle. The `area()` function takes the radius of the circle as input and returns the area of the circle. The `perimeter()` function also takes the radius of the circle as input and returns the perimeter of the circle.

**Function Descriptions**

### `area(r)`

The `area()` function calculates the area of a circle using the formula `πr^2`.

**Call Example:**

```python
area = circle.area(5)
print(area)
```

This code will print the following output:

```
78.53981633974483
```

### `perimeter(r)`

The `perimeter()` function calculates the perimeter of a circle using the formula `2πr`.

**Call Example:**

```python
perimeter = circle.perimeter(5)
print(perimeter)
```

This code will print the following output:

```
31.41592653589793
```

## rectangle.py


**General Description**

The `rectangle.py` module provides two functions for calculating the area and perimeter of a rectangle. The `area()` function takes the length and width of the rectangle as input and returns the area of the rectangle. The `perimeter()` function also takes the length and width of the rectangle as input and returns the perimeter of the rectangle.

**Function Descriptions**

### `area(l, w)`

The `area()` function calculates the area of a rectangle using the formula `l * w`.

**Call Example:**

```python
area = rectangle.area(5, 3)
print(area)
```

This code will print the following output:

```
15
```

### `perimeter(l, w)`

The `perimeter()` function calculates the perimeter of a rectangle using the formula `2(l + w)`.

**Call Example:**

```python
perimeter = rectangle.perimeter(5, 3)
print(perimeter)
```

This code will print the following output:

```
16
```

## square.py 

**General Description**

The `square.py` module provides two functions for calculating the area and perimeter of a square. The `area()` function takes the side length of the square as input and returns the area of the square. The `perimeter()` function also takes the side length of the square as input and returns the perimeter of the square.

**Function Descriptions**

### `area(a)`

The `area()` function calculates the area of a square using the formula `a * a`.
**Call Example:**

```python
area = square.area(5)
print(area)
```

This code will print the following output:

```
25
```
### `perimeter(a)`

The `perimeter()` function calculates the perimeter of a square using the formula `4 * a`.
**Call Example:**

```python
perimeter = square.perimeter(5)
print(perimeter)
```

This code will print the following output:

```
20
```

## triangle.py

**General Description**

The `triangle.py` module offers two functions for determining the area and perimeter of a triangle. The `area()` function takes the triangle's base and height as input and returns the triangle's area. The `perimeter()` function also takes the lengths of the triangle's three sides as input and returns the triangle's perimeter.

**Function Descriptions**

### `area(a, h)`

The `area()` function computes the area of a triangle using the formula `(base * height) / 2`.

**Call Example:**

```python
area = triangle.area(5, 3)
print(area)
```

This code will print the following output:

```
7.5
```

### `perimeter(a, b, c)`

The `perimeter()` function calculates the perimeter of a triangle using the formula `a + b + c`, where `a`, `b`, and `c` represent the lengths of the triangle's three sides.

**Call Example:**

```python
perimeter = triangle.perimeter(5, 3, 4)
print(perimeter)
```

This code will print the following output:

```
12
```

## Changelog

### d481b3d477a69e468092aebfab3778f1933e5fa9 
* Rearrange: .DS_Store banished!

### b50efb945977dcecfc462d8b13c212ff2e175b12
* Docs: Added documentation for all functions.

### 9b70cee18a4add8639315df126bcbee09ab7877c
* Fix: Fixed rectangle perimeter calculation.

### 75460d579600d99ed97a73393bd2521283dc1451
* Feat: Added calculations for the Triangle shape.

### adf5a2a6652783bc358ac4b8c09f9f7a5a39b15e
* Feat: Added calculations for the Rectangle shape.
