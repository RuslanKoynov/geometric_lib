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
___
# Общее описание решения
Проект «geometric_lib» представляет собой библиотеку для вычисления площади и периметра геометрических фигур.

## Описание функций
### Функция `circle`

Функция `circle` выполняет следующую задачу:

- Принимает число r и возвращает площадь круга
- Принимает число r и возвращает периметр круга

Пример использования функции `circle`:
```python
import math
'''Принимает число r и возвращает площадь круга'''
def area(r):
    return math.pi * r * r

'''Приннимает число r и возвращает периметр круга'''
def perimeter(r):
    return 2 * math.pi * r
```
```markdown
Input:
  r = 5

Output:
  Area = 78.5
  Perimetr = 22
```
___

### Функция `rectangle`

Функция `rectangle` выполняет следующую задачу:

- Принимает a, b и возвращает площадь прямоугольника
- Принимает a, b и возвращает периметр прямоугольника

Пример использования функции `rectangle`:

```python
''' Принимает числа a, b и возвращает площадь стороны a и b '''
def area(a, b):
    return a * b
''' Принимает числа a, b и возвращает периметр стороны a и b '''
def perimeter(a, b):
    return a * 2 + b * 2
```
```markdown
Input:
  a = 5
  b = 4

Output:
  Area = 20
  Perimetr = 18
```

### Функция `square`

Функция `square` выполняет следующую задачу:

- Принимает число n и возвращает площадь квадрата
- Принимает число n и возвращает периметр квадрата

Пример использования функции `square`:

```python
''' Принимает число a и возвращает площадь квадрата '''
def area(a):
    return a * a

''' Принимает число a и возвращает периметр квадрата '''
def perimeter(a):
    return 4 * a
```
```markdown
Input:
  a = 5

Output:
  Area = 25
  Perimetr = 20
```
### Функция `triangle`

Функция `triangle` выполняет следующую задачу:

- Принимает числа a, h и возвращает площадь треугольника
- Принимает числа a, b, c и возвращает периметр треугольника

Пример использования функции `triangle`:

```python
''' Принимает числа a, h и возвращает площадь треугольника'''
def area(a, h):
    return a * h / 2
'''Принимает числа a, b, c и возвращает периметр треугольника'''
def perimeter(a, b, c): 
    return a + b + c
```
```markdown
Input:
  a = 5
  b = 3
  c = 4
  h = 3

Output:
  Area = 7.5
  Perimetr = 12
```
# История изменения проекта с хэшами 

commit b8960cb31d12c2bf259be07df9d92fb3328782ca (HEAD -> tests_409512)
Author: Ruslan Sanigullin <409512@niuitmo.ru>
Date:   Wed Nov 29 17:11:58 2023 +0300

    test: unittests added

 .DS_Store                                      | Bin 10244 -> 10244 bytes
 .idea/.gitignore                               |   3 ++
 .idea/geometric_lib.iml                        |   8 ++++++
 .idea/inspectionProfiles/profiles_settings.xml |   6 ++++
 .idea/misc.xml                                 |   7 +++++
 .idea/modules.xml                              |   8 ++++++
 .idea/vcs.xml                                  |   6 ++++
 circle.py                                      |  37 ++++++++++++++++++++++++-
 rectangle.py                                   |  35 +++++++++++++++++++++++
 square.py                                      |  31 +++++++++++++++++++++
 triangle.py                                    |  35 +++++++++++++++++++++++
 11 files changed, 175 insertions(+), 1 deletion(-)

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Thu Nov 2 00:56:21 2023 +0300

    docs: added documentation to triangle.py

commit b0740b51f8b7de5d7a53787c02efb27a8f714939

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Thu Nov 2 00:56:01 2023 +0300

    docs: added documentation to square.py

commit 4f9e2b7db18d28c11e9f767d9a546ea897131213

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Thu Nov 2 00:55:35 2023 +0300

    docs: added documentation to rectangle.py

commit cb5c7d24056f4052b5ae21c21341186d70e4f89e

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Thu Nov 2 00:55:12 2023 +0300

    docs: added documentation to circle.py
commit 515305dc429e8f9a428b3e13cfb97662a7fb8f37 (origin/main, origin/HEAD, main)

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Tue Oct 3 00:51:37 2023 +0300

    in the <rectangle.py> mistake is fixed

commit 6da924381d1fe7ab7a3be332e00075d7b9422db4

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Tue Oct 3 00:50:25 2023 +0300

    <triangle.py> added and code is created

commit b051d9607c25b9c170899a5ae816dc3e69c8a909

Author: Ruslan Sanigullin <409512@niuitmo.ru>

Date:   Tue Oct 3 00:49:34 2023 +0300

    <rectangle.py> added and code is created

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2

Author: smartiqa <info@smartiqa.ru>

Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460

Author: smartiqa <info@smartiqa.ru>

Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added



## UnitTest
#### Всего сделано 30 теста: 22 успешных, 8 неуспешных

### Circle.py
###### correct tests
- area()
~~~
input: 0
output: 0
~~~
~~~
input: 5
output: 78.5398163397448
3
~~~
- perimeter()
~~~
input: 0
output: 0
~~~
~~~
input: 5
output: 31.41592653589793
~~~
###### uncorrect tests
- area()
~~~
input: -5
output: 78.53981633974483
expected: the radius cannot be negative
~~~
- perimeter()
~~~
input: -5
output: -31.41592653589793
expected: the radius cannot be negative
~~~

### Reactangle.py
###### correct tests
- area()
~~~
input: 2, 3
output: 6
~~~
~~~
input: 0, 3
output: 0
~~~
~~~
input: 5.5, 2
output: 11
~~~
- perimeter()
~~~
input: 2, 3
output: 10
~~~
~~~
input: 0, 3
output: 6
~~~
~~~
input: 5.5, 2
output: 15
~~~
###### uncorrect tests
- area()
~~~
input: 5, -4
output: -20
expected: error: a or b can not be negative
~~~
- perimeter()
~~~
input: 5, -4
output: 2
expected: error: a or b can not be negative
~~~

### Square.py
###### correct tests
- area()
~~~
input: 4
output: 16
~~~
~~~
input: 0
output: 0
~~~
~~~
input: 4.5
output: 20.25
~~~
- perimeter()
~~~
input: 4
output: 16
~~~
~~~
input: 4.5
output: 18.0
~~~
~~~
input: 0
output: 0
~~~
###### uncorrect tests
- area()
~~~
input: -4
output: 16
expected: a can not be negative
~~~
- perimeter()
~~~
input: -4
output: -16
expected: a can not be negative
~~~

##### Triangle.py
###### correct tests
- area()
~~~
in: 4, 5
out: 10.0
~~~
~~~
in: 4, 0
out: 0
~~~
~~~
in: 4, 5.5
out: 0
~~~
- perimeter()
~~~
in: 4, 5, 6
out: 15
~~~
~~~
in: 4, 5, 0
out: 9
~~~
~~~
in: 4, 5,5, 6
out: 15.5
~~~
###### uncorrect tests
- area()
~~~
in: 4, -5
out: -10.0
expected: a or b can not be negative
~~~
- perimeter()
~~~
in: 4, 5, -6
out: 3
expected: a or b can not be negative
~~~
## autotests success:
- all tests: 30
- tests with errors: 8
- tests without errors: 22
~~~
tests with errors - 8/30 = 26.6667%
tests without errors - 22/30 = 73.3333%
~~~