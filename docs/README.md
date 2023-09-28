# General description

1. Clone global repository for local
2. Added other files with program for calculate area and perimeter.
3. Used commits and push for secure our project.
4. After all, merge main branch with other branch and pull request.


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



## Repositorys history

### 1. Commit

Hash: 8ba9aeb3cea847b63a91ac378a2a6db758682460

#### Message:
> Circle and square added

### 2. Commit

Hash: d078c8d9ee6155f3cb0e577d28d337b791de28e2

#### Message:
> Docs added

### 3. Commit

Hash: 148115a95af31481ca494d5caf2bb4ea110e2b4d

#### Message:
>  rectangle.py added

### 4. Commit

Hash: cff750c270a242f369d3a4bee44bd93378b89357

#### Message:
>  triangle.py fixed

