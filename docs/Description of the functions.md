## Description of the functions

### In programs, we used math formulas:

#### Area

1. Circle: S = πR²
2. Rectangle: S = ab
3. Square: S = a²
4. Triangle: S = ah/2

#### Perimeter

1. Circle: P = 2πR
2. Rectangle: P = 2a + 2b
3. Square: P = 4a
4. Triangle: P = a + b + c

### Functions

### Circle: 

1. def area(r):


    return math.pi * r * r

2. def perimeter(r):



    return 2 * math.pi * r


> r (int) - circles radius 
> 
##### example(1): 

r = 10

print(area)

**we get: (10^2 * π) = 314,15926535897932384626433832795**

#### example(2): 

r = 10

print(perimeter)

**we get: (20 * π) = 62,83185307179586476925286766559**

### Rectangle:

1. def area(a, b):


    return a * b

2. def perimeter(a, b):


    return (a + b) * 2

> a(int) - first side of rectangle 
> 
> b(int) - second side of rectangle 

##### example(1): 

a = 5, b = 10

print(area)

**we get: (5*10) = 50**

##### example(2): 

a = 5, b = 10

print(perimeter)

**we get: ((5+10)2) = 30**

### Square:

1. def area(a):


    return a * a


2. def perimeter(a):


    return 4 * a

> a(int) - side of square

##### example(1):

a = 10

print(area)

**we get: (10*10) = 100**

##### example(2):

a = 10

print(area)

**we get: (4*10) = 40**

### Triangle:

1. def area(a):


    return a * h / 2

2. def perimeter(a, b, c):


    return a + b + c

> a(int) - first side of triangle
> 
> b(int) - second side of triangle
> 
> c(int) - hypotenuse 
> 
> h - height of triangle

##### example(1):

a = 6, b = 8, h = 8, c = 10

print(area)

**we get: ((6*8)/2) = 24**

##### example(2):

a = 6, b = 8, h = 8, c = 10

print(area)

**we get: (6+8+10) = 24**