# General description
- includes functions of area and perimeter of 4 shapes, using math formulas 
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Function descriptions
## Circle
### area(r)
- Arguments: r (int) - radius
- Return value: math.pi * r * r (int) - area
- Example: **area(_10_)**
> 314
### perimeter(r)
- Arguments: r (int) - radius
- Return value: 2 * math.pi * r (int) - perimeter
- Example: **perimeter(_10_)**
> 62.83

## Rectangle
### area(a, b)
- Arguments: a, b (int) - sides
- Return value: a * b (int) - area
- Example: **area(_5, 6_)**
> 30
### perimeter(a, b)
- Arguments: a, b (int) - sides
- Return value: (a + b) * 2 (int) - perimeter
- Example: **perimeter(_5, 6_)**
> 22

## Square
### area(a)
- Arguments: a (int) - side
- Return value: a * a (int) - area
- Example: **area(_8_)**
> 64
### perimeter(a)
- Arguments: a(int) - side
- Return value: 4 * a (int) - perimeter
- Example: **perimeter(_8_)**
> 32

## Triangle
### area(a, h)
- Arguments: a (int) - side; h (int) - height
- Return value: a * h / 2 (int) - area
- Example: **area(_6, 4_)**
> 12
### perimeter(a, b, c)
- Arguments: a, b, c (int) - sides
- Return value: a + b + c (int) - perimeter
- Example: **perimeter(_5, 6, 7_)**
> 18

# Project history 
- commit 5d15427935ba1117d9fdab3a4331c85ad80b2284 (HEAD -> documentation_408483)
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Sun Oct 8 15:36:29 2023 +0300
>
>   docs: changes in documentation of rectangle and square

- commit 807c5530244316840b780debbafb8d1511840ffc
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Sun Oct 8 15:33:57 2023 +0300
>
>   docs: documentation to triangle added

- commit 7a04efdfe87c666c5edc554ba330b6c0d7c50bbf
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Sun Oct 8 15:31:06 2023 +0300
>
>   docs: documentation to square added

- commit 7ce471fbabe5b60d2fbf17308eb923fffc85a251
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Sun Oct 8 15:27:56 2023 +0300
>
>   docs: documentation to rectangle added

- commit e7ef9b51ee42316b1182a19532e5ddb9fba1adc1
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Sun Oct 8 15:23:05 2023 +0300
>
>   docs: documentation to circle added

- commit 8a6bb837f79ced2be3781a965b532e9da26daf28
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Thu Sep 21 18:33:41 2023 +0300
>
>   fix: fixed rectangle perimeter; feat: added triangles

- commit 073962c87072826f0dfbaec008b7bb62911f22f0
> Author: Vsovolod Grachev <vsevolod1607@bk.ru>
> Date: Thu Sep 21 18:30:22 2023 +0300
>
>   feat: added rectangles

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
> Author: smartiqa <info@smartiqa.ru>
> Date: Thu Mar 4 14:55:29 2021 +0300
>
>   L-03: Docs added

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
> Author: smartiqa <info@smartiqa.ru>
> Date: Thu Mar 4 14:54:08 2021 +0300
>
>   L-03: Circle and square added