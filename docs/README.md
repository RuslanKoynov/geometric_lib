# Geometric lib
## Общее описание решения
Geometric lib - это библиотека с программами, с помощью которых вы можете вычислять периметры и площади различных математических фигур.
## Математические формулы
### Площади:
- Квадрат: S = a²
- Прямоугольник: S = a * b
- Треугольник: S = a * h / 2
- Круг: S = π * R²

### Периметры:
- Квадрат: P = 4 * a
- Прямоугольник: P = 2 * a + 2 * b
- Тругольник: P = a + b + c
- Круг: P = 2π * R
## Описание функций
### square.py
```python
def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает площадь квадрата, вычисляя ее по формуле: a ^ 2
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает периметр квадрата, вычисляя его по формуле: 4 * a
    '''
    return 4 * a
```
### rectangle.py
```python
def area(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает площадь прямоугольника, вычисляя ее по формуле: a * b
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает периметр прямоугольника, вычисляя его по формуле: a * b
    '''
    return (a + b) * 2
```
### triangle.py
```python
def area(a, h):
    '''
    Принимает два числа, которые являются стороной и высотой треугольника: h, a
    Возвращает площадь треугольника, вычисляя ее по формуле: 1/2 * a * h
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает три числа, которые являются сторонами треугольника: a, b, c
    Возвращает периметр треугольника, вычисляя его по формуле: a + b + c
    '''
    return a + b + c

```
### circle.py
```python
import math
'''
Библиотека math является стандартной в Python и содержит много полезных математических функций и констант.
Например: работа с вещественными числами(плавающей точкой).
'''

def area(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает площадь круга, вычисляя ее по формуле: π * r ^ 2
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: 2 * π * r
    '''
    return 2 * math.pi * r
```
## Примеры использования функций
### square.py
<img src="https://ie.wampi.ru/2023/10/04/IZOBRAZENIE_2023-10-04_150205156.png" alt="IZOBRAZENIE_2023-10-04_150205156.png" border="0">

### rectangle.py
<img src="https://im.wampi.ru/2023/10/04/IZOBRAZENIE_2023-10-04_150406819.png" alt="IZOBRAZENIE_2023-10-04_150406819.png" border="0">

### triangle.py
<img src="https://ic.wampi.ru/2023/10/04/IZOBRAZENIE_2023-10-04_150546020.png" alt="IZOBRAZENIE_2023-10-04_150546020.png" border="0">

### circle.py
<img src="https://ic.wampi.ru/2023/10/04/IZOBRAZENIE_2023-10-04_150707357.png" alt="IZOBRAZENIE_2023-10-04_150707357.png" border="0">
:heartpulse:

## История изменения проекта
```bash
commit a8a4c578c99198a64ec313faee0c0a25f768d352 (HEAD -> main)
Author: beth <nikas-cat@yandex.ru>
Date:   Wed Oct 4 15:12:16 2023 +0400

    documented

commit 13125adda5fe908b8492f3a125704e5e6677ae0a (origin/main, origin/HEAD)
Merge: d078c8d ba8a149
Author: beth <102821957+bethqqe@users.noreply.github.com>
Date:   Wed Sep 20 15:54:53 2023 +0400

    Merge pull request #1 from bethqqe/new_features_408616

    New features 408616

commit ba8a1498f44fc55f212ac8235dbfc8582c3ddf66 (origin/new_features_408616)
Author: beth <nikas-cat@yandex.ru>
Date:   Thu Sep 14 22:20:32 2023 +0300

    Changed an error in calculating the perimeter of a rectangle

commit a787f6daa93cc024d200c0767815ef5f1c336f33
Author: beth <nikas-cat@yandex.ru>
Date:   Thu Sep 14 21:42:40 2023 +0300

    added new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
```
