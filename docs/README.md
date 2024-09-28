# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# General description

**This project defines functions for calculating areas and perimeters for ***circles, triangles, squares, rectangles***.**

## Functions description

### Circle's functions

#### `area(r)`

**calculates the area of a circle also in float numbers.**

**takes the radius of a circle.**

_function call example_
```python
from circle import area

r = 9.23
a = area(r)
#  a = 267.6413887780099
```

#### `perimeter(r)`

**calculates the perimeter of a circle also in float numbers.**

**takes the radius of a circle.**

_function call example_
```python
from circle import perimeter

r = 9.23
a = perimeter(r)
#  a = 57.99380038526758
```

### Rectangle's functions

#### `area(a, b)`

**calculates the area of a rectangle also in float numbers.**

**takes the width and length of a rectangle in any order.**

_function call example_
```python
from rectangle import area

width = 12.5
length = 20.3
result = area(length, width)
# result = 253.75
```

#### `perimeter(a, b)`

**calculates the perimeter of a rectangle also in float numbers.**

**takes the width and length of a rectangle in any order.**

_function call example_
```python
from rectangle import perimeter

width = 12.5
length = 20.3
result = perimeter(length, width)
# result = 65.6
```

### Square's functions

#### `area(a)`

**calculates the area of a square also in float numbers.**

**takes the side of the square.**

_function call example_
```python
from square import area

side = 12.5
result = area(side)
# result = 156.25
```

#### `perimeter(a)`

**calculates the perimeter of a square also in float numbers.**

**takes the side of the square.**

_function call example_
```python
from square import perimeter

side = 12.5
result = perimeter(side)
# result = 50.0
```

### Trinagle's functions

#### `area(a, h)`

**calculates the area of a trinagle also in float numbers.**

**takes the height and side of the triangle to which the height is drawn.**

_function call example_
```python
from trinagle import area

side = 12.5
height = 3.23
result = area(side, height)
# result 20.1875
```

#### `perimeter(a, b, c)`

**calculates the perimeter of a trinagle also in float numbers.**

**takes three sides of a triangle.**

_function call example_
```python
from trinagle import perimeter

first_side = 12.5
second_side = 3.23
third_side = 12
result = perimeter(first_side, second_side, third_side)
#  output = 27.73
```

### Tests

| Название теста                  | Входные данные                    | Ожидаемый результат                                   | Статус |
|---------------------------------|-----------------------------------|-------------------------------------------------------|--------|
| Circle - test_less_than_zero    | -12, -12                          | "Input data ERROR: radius cannot be negative or zero" | True   |
| Circle - test_not_number        | "hi", "hi"                        | "Input data ERROR: radius must be a number"           | True   |
| Circle - test_zero              | 0, 0                              | "Input data ERROR: radius cannot be negative or zero" | True   |
| Circle - test_float_type        | 3.12, 3.44                        | 30.5815, 21.6142                                      | True   |
| Circle - test_int_type          | 3, 3                              | 28.2743, 18.8496                                      | True   |
| Circle - test_bool_type         | True, False                       | "Input data ERROR: radius must be a number"           | True   |
| Rectangle - test_less_than_zero | (-1, 321), (-100, -901)           | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Rectangle - test_zero           | (0, 5), (5, 0)                    | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Rectangle - test_not_number     | (19, "hi"), ("hi", 19)            | "Input data ERROR: sides must be a number"            | True   |
| Rectangle - test_int_type       | (2, 3), (8, 8)                    | 6, 32                                                 | True   |
| Rectangle - test_float_type     | (15.3, 13), (15.3, 13)            | 198.9, 56.6                                           | True   |
| Rectangle - test_bool_type      | (True, 10), (10, False)           | "Input data ERROR: sides must be a number"            | True   |
| Square - test_less_than_zero    | -1, -100                          | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Square - test_zero              | 0, 0                              | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Square - test_not_number        | "hi", "hi"                        | "Input data ERROR: sides must be a number"            | True   |
| Square - test_int_type          | 2, 8                              | 4, 32                                                 | True   |
| Square - test_float_type        | 15.3, 15.3                        | 234.09, 61.2                                          | True   |
| Square - test_bool_type         | True, False                       | "Input data ERROR: sides must be a number"            | True   |
| Triangle - test_less_than_zero  | (-1, 10), (-100, 19, -10000)      | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Triangle - test_zero            | (0, 9), (1, 0, 8)                 | "Input data ERROR: sides cannot be negative or zero"  | True   |
| Triangle - test_not_number      | ("hi", 12), (12, "hi" 3)          | "Input data ERROR: sides must be a number"            | True   |
| Triangle - test_int_type        | (12, 6), (5, 8, 10)               | 36, 23                                                | True   |
| Triangle - test_float_type      | (15.3, 16.0), (15.3, 13.4, 6.989) | 122.4, 35.686                                         | True   |
| Triangle - test_bool_type       | (True, 90), (3, False, 9)         | "Input data ERROR: sides must be a number"            | True   |
| Triangle - test_not_triangle    | (10, 90), (3, 90, 9)              | 450, "ERROR: this is not a triangle"                  | True   |
# History of project changes
 |**Hash**                                | **Author**                            |  **Comments**                   |
 | ----------------------------------------|:-------------------------------------:| -----------------------------:  |
 | 5efeed22b36eae527d43edd41f82d988d7e946c7| x3pio <x300mark@gmail.com>           |fixed bug in rectangle function  |
 | b50db8ebd7a1006bc997cbd86f37b002cc1afb94| x3pio <x300mark@gmail.com>           | new file for rectangle functions                |
 | d078c8d9ee6155f3cb0e577d28d337b791de28e2| smartiqa <info@smartiqa.ru> |  Docs added                          |
 | 8ba9aeb3cea847b63a91ac378a2a6db758682460| smartiqa <info@smartiqa.ru> |  Circle and square added|
 




