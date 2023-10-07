# Repository with .py files for counting areas and perimiters of triangle, square and rectangle

## Math formulas, used in files:

### Area
- Circle: S = πR²
- Triangle: S = ah/2
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Triangle: P = a + b + c
- Rectangle: P = 2a + 2b
- Square: P = 4a

## General description of the solution:

### Files situated in the repository:
- rectangle.py
- triangle.py
- square.py
- circle.py
- \docs\README.md

## Functions' descriptions:

## rectangle.py

### Area:
Takes the numbers a and b, returns their product
Parameters:
    a (int, float, etc...) first number
    b (int, float, etc...) the second number
Return value:
    a_b_multiplied (int, float, etc...) product of numbers a and b
Example of a function call:
    input >> 2, 3
    output << 6

### Perimeter:
Takes the numbers a and b, returns their doubled sum
Parameters:
    a (int, float, etc...) first number
    b (int, float, etc...) the second number
Return value:
    a_b_summa_doubled (int, float, etc...) the doubled sum of the numbers a and b
Example of a function call:
    input >> 2, 3
    output << 10

## square.py

### Area:
Takes a number n, returns its square
Parameters:
    a (int, float, etc...) number
Return value:
    a_squared (int, float, etc...) the square of the number a
Example of a function call:
    input >> 2
    output << 4

### Perimeter:
Takes the number n, returns it multiplied by 4
Parameters:
    a (int, float, etc...) number
Return value:
    a_multiplied_by_4 (int, float, etc...) the number a multiplied by 4
Example of a function call:
    input >> 2
    output << 8

## triangle.py

### Area:
Accepts the numbers a and h, returns their semi-reproduction
Parameters:
    a (int, float, etc...) the first number
    h (int, float, etc...) the second number
Return value:
    a_h_multiplied_half (int, float, etc...) semi-reproduction of numbers a and h
Example of a function call:
    input >> 2, 3
    output << 3

### Perimeter:
Accepts the numbers a b and c, returns their sum
Parameters:
    a (int, float, etc...) first number
    b (int, float, etc...) the second number
    c (int, float, etc...) the third number
Return value:
    a_b_c_summ (int, float, etc...) sum of numbers a,b,c
Example of a function call:
    input >> 3, 4, 5
    output << 12

## circle.py

### Area:
*import the math library to get the number pi
Takes the number r, returns its square multiplied by pi
Parameters:
    r (int, float, etc...) first number
Return value:
    a_squres_multiplied_by_pi (float, etc...) the square of the number r multiplied by the number pi
Example of a function call:
    input >> 3
    output << 28.274333882308138

### Perimeter:
*import the math library to get the number pi
Takes the number r, returns it multiplied by twice the number pi
Parameters:
    r (int, float, etc...) first number
Return value:
    a_multiplied_by_double_pi (float, etc...) the number r multiplied by twice the number pi
Example of a function call:
    input >> 2
    output << 12.566370614359172

## Additional info:

This documentation was modified using [Visual Studio Code](https://code.visualstudio.com/).

> [!NOTE]
> This file stores the history of changes to the project with the hashes of the comits except the last one.
