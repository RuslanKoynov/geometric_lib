# Geometric lib
## Общее описание решения
**Geometric lib** - это библиотека с программами, с помощью которых вы можете вычислять периметры и площади различных форм.
## Математические формулы
### Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = ah / 2

### Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c
## Описание функций
### Circle.py
1. **Area**
    - ***S=πR²*** - формула площади круга
    - ***import math*** - предоставляет обширный фунционал для проведения вычислений с
вещественными числами (числами с плавающей точкой)
    - ***r*** - радиус круга
    - ***math.pi*** - математическая константа

1. **Perimeter**
     - ***P = 2πR*** - формула периметра круга
     - ***import math*** - предоставляет обширный фунционал для проведения вычислений с
вещественными числами (числами с плавающей точкой)
     - ***r*** - радиус круга
     - ***math.pi*** - математическая константа
  
### Rectangle.py
1. **Area**
    - ***S = ab*** - формула площади прямоугольника
    - ***a,b*** - стороны прямоугольника (длина и  ширина)

1. **Perimeter**
     - ***P = 2a + 2b*** - формула периметра прямоугольника
     - ***a,b*** - стороны прямоугольника (длина и ширина)
  
### Square.py
1. **Area**
    - ***S = a²*** - формула площади квадрата
    - ***а*** - сторона квадрата

1. **Perimeter**
     - ***P = 4a*** - формула периметра квадрата
     - ***а*** - сторона квадрата
   
### Triangle.py
1. **Area**
    - ***S = ah / 2*** - формула площади прямоугольника
    - ***a,b,c*** - стороны треугольника 
    - ***h*** - высота треугольника

1. **Perimeter**
     - ***P = a + b + c*** - формула периметра прямоугольника
     - ***a,b,c*** - стороны треугольника 
     - ***h*** - высота треугольника
## Примеры использования функций
### Circle.py
1. **Пример кода**
```
import math
'''
Модуль math предоставляет обширный фунционал для проведения
вычислений с вещественными числами (числами с плавающей точкой)
'''

def area(r):
    '''
    Принимает число, которое является радиусом круга
    Возвращает площадь круга, вычисляя ее по формуле: S=π *r^2
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Принимает число, которое является радиусом круга
    Возвращает площадь круга, вычисляя ее по формуле: P=2πr
    '''
    return 2 * math.pi * r
```
3. **Вывод**
```
r=10
area = 314.1592653589793; perimeter = 62.83185307179586
```
### Rectangle.py
1. **Пример кода**
```
def area(a, b):
    '''
    Принимает числа, которые являются сторонами прямоугольника
    Возвращает площадь прямоугольника, вычисляя ее по формуле: S=ab
    '''
    return a * b
def perimeter(a, b):
    '''
    Принимает числа, которые являются сторонами прямоугольника
    Возвращает периметр прямоугольника, вычисляя ее по формуле: P=2a+2b
    '''
    return 2*a + 2*b
```
3. **Вывод**
```
a=5
b=7
area = 35; perimeter = 24
```
### Square.py
1. **Пример кода**
```
def area(a):
    '''
    Принимает число, которое является стороной квадрата
    Возвращает площадь квадрата, вычисляя ее по формуле: S=a*a
    '''
    return a * a

def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата
    Возвращает периметр квадрата, вычисляя его по формуле: P=4*a
    '''
    return 4 * a
```
3. **Вывод**
```
a=5
area = 25; perimeter = 20
```
### Triangle.py
1. **Пример кода**
```
def area(a, h):
    '''
    Принимает числа, которые являются стороной и высотой треугольника
    Возвращает площадь треугольника, вычисляя ее по формуле: S=ah/2
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
    Принимает числа, которые являются стороной и высотой треугольника
    Возвращает периметр треугольника, вычисляя его по формуле: S=a+b+c
    '''
    return a + b + c
```
3. **Вывод**
```
a=2
b=4
c=5
h=2
area = 3; perimeter = 12
```
## Тестирование через unit test
### Этот проект содержит модули тестирования через unit test для расчета площади и периметра круга, прямоугольника, квадрата и треугольника:
  - Круг: circletest.py
  - Прямоугольник: rectest.py
  - Квадрат: squaretest.py
  - Треугольник: triangletest.py
### Пример кода проверки для circle.py:
```
import unittest
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_with_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_with_square(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_area_with_random_number(self):
        res=area(28)
        self.assertEqual(res, 2463.0086404143976)

    def test_perimeter_with_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_with_square(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_with_random_number(self):
        res=perimeter(31)
        self.assertEqual(res,194.77874452256717)

if __name__ == '__main__':
    unittest.main()
```
### Пример вывода через командную строку:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
## Commit history
commit 245193d34fc43ba97c128fa91d42ebef32db6164
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Tue Nov 14 21:58:47 2023 +0300

    modified tests for circle,square and added tests for triangle

commit e72601c0733618419c2c124f15d2617fca67a944
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Tue Nov 14 21:53:12 2023 +0300

    added tests for square

commit a0ca828917873818057cc71fab988a7f68db02df
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Tue Nov 14 21:50:21 2023 +0300

    added test for circle

commit 53ed38611dd8920f62a43a32618a26908fa23e04
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Tue Nov 14 21:30:27 2023 +0300

    added tests for rectangle.py

commit 250e31befe11be6928a12d025dcba558c449c1b5 (HEAD -> main, origin/main, origin/HEAD)
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Wed Oct 4 14:06:49 2023 +0300

    File declaration
    
commit 1555f29e73ac47684fe55389f276019aa701daac (HEAD -> main, origin/main, origin/HEAD)
Author: vikaleks <68038711+vikaleks@users.noreply.github.com>
Date:   Wed Oct 4 10:49:29 2023 +0300

    Update README.md

commit 8aa44992ba475e733998de92ffaa9db9fbbf1035
Author: vikaleks <68038711+vikaleks@users.noreply.github.com>
Date:   Wed Oct 4 01:19:46 2023 +0300

    Update README.md

commit ad5c568e1c11e661d526a8500a8f04b54dd1f0d8 (test, new)
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Mon Sep 18 21:41:08 2023 +0300

    fixed rectangle.py

commit 6d7d570213c566aa4f4f55a40df75bd8a60d1461
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Mon Sep 18 21:39:12 2023 +0300

    added new file traingle.py

commit 63c3e89e38aad9d117424efa3eeb0850c52614c6
Author: vikaaaleks <vikaaaleks@mail.ru>
Date:   Mon Sep 18 21:35:21 2023 +0300

    added new file rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (upstream/main, upstream/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
