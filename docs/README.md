# Functions for calculation of the area and perimeter of the figure

## Formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*(h / 2)

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c


## Functions
### Circle
- **area**: takes a number r, returns the area of a circle with radius r

- - Function: area(r)
- - Example: area(2) = 12.5836

- **perimeter**: takes a number r, returns the perimeter (circumference) of a circle with radius r

- - Function: perimeter(r)
- - Example: perimeter(10) = 62.918


### Rectangle
- **area**: takes numbers a and b, returns the area of a rectangle with given lenght of a and b

- - Function: area(a, b)
- - Example: area(5, 10) = 50


- **perimeter**: takes numbers a and b, returns the perimeter of a rectangle with given lenght of a and b

- - Function: perimeter(a, b)
- - Example: perimeter(4, 4) = 16


### Square
- **area**: takes a number a, returns the area of a square with the given length of a and b

- - Function: area(a)
- - Example: area(7) = 49


- **perimeter**: takes a number a, returns the perimeter of a square with the given length of a

- - Function: perimeter(a)
- - Example: perimeter(12) = 48


### Triangle
- **area**: takes numbers a and h, returns the area of a triangle with the given lenght of a and h

- - Function: area(a, h)
- - Example: area(2) = 10


- **perimeter**: takes numbers a, b, and c, returns the perimeter of a triangle with the given lenght of a, b and c

- - Function: perimeter(a, b, c)
- - Example: perimeter(1, 2, 3) = 6


## History of commits
### 5417d85
- added rectangle.py
### da809b3
- fix error in triangle.py
### 7f0a254
- merge 2 branches
### 8c4ab9e
- added report
### 2080cb1
- added ID.txt