# Документация
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S=(ah)/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P=a+b+c

## Описание решения
1.Функция принимает значение
	
2.Выполняется математическая операция с введенным значением

3.Выводится результат
## Описание каждой функции с примерами вызова
### Circle
***programm:***
```python
import math

'''
    Модуль дающий возможность работать с числами в расширенном функционале
    '''



def area(r):
    '''
    r: число обозначащее радиус круга
    Возвращаемое значение:
            число Пи умноженное на квадрат числа r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    r: число обозначающее радиус круга
    Возвращаемое значение:
            удвоенное произведение числа Пи и числа r
    '''
    return 2 * math.pi * r
```
 ***call:***
 *Input:* r=7
 *Output:* S=153.938040, P=43.982297
 ### Rectangle
 ***programm:***
```python
def area(a, b):
    '''
        Возвращает произведение двух чисел.
            Параметры:
                    a: первое число
                    b: второе число
            Возвращаемое значение:
                    area: число равное произведению a и b (площадь прямоугольника)
        '''
    return a * b


def perimeter(a, b):
    return 2*(a + b)
'''
    Возвращает произведение удвоенную сумму двух чисел.
            Параметры:
                    a: первое число
                    b: второе десятичное число
            Возвращаемое значение:
                perimeter: число равное удвоенной сумме a и b
    '''
```
***call:***
*Input:* a=2, b=5
*Output:* S=10, P=14
### Square
```python
def area(a):
    '''
    a: сторона квадрата
    Возвращаемое значение: квадрат числа a (площадь квадрата)
    '''
    return a * a


def perimeter(a):
    '''
    a: сторона квадрата
    Возвращаемое значение: квадрат числа a (периметр квадрата)
    '''
    return 4 * a
```
***call:***
*Input:* a=6
*Output:* S=36,P=24
### Triangle
```python
def area(a, h):
    '''
    a: сторона треугольника
    h: высота треугольника
    Возвращаемое значение: произведение a и h деленное на два
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    a: сторона треугольника
    b: сторона треугольника
    c: сторона треугольника
    Возвращаемое значение: сумма трех чисел a,b и с
    '''
    return a + b + c

```
***call:***
*Input:* a=5, h=10, b=7, c=2
*Output:* S=25, P=14

## История изменений с хешами комитов(без последнего)

commit 2c85460a17bcd0ab1584398d834d27606f94cb62
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 11:29:01 2023 +0300

    docs:added documentation to README

commit 2fa044f270248a73a2d67628324f34498509b8c2
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 10:55:23 2023 +0300

    docs:added documentation to rectangle

commit 01e85d6a804c8c93ae8ad3814cb4f37f5bb80ad5
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 10:54:45 2023 +0300

    docs:added documentation to triangle

commit 0d660e2ff88132ad844d9adbac9fc6ff8a034d03
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 10:41:22 2023 +0300

    docs:added documentation to triangle

commit eb045a5dc5841cda1004961f59bdf7db1c3bf37f
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 10:27:44 2023 +0300

    docs:added documentation to square

commit 012388c92bbecbb13aecc5870204d7d102c3e1fe
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 10:12:43 2023 +0300

    docs:added documentation to circle

commit 822cfa84360add54150e019a16ba558f07f7a3ce
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Oct 5 09:54:54 2023 +0300

    docs:added documentation to rectangle

commit 100dc9c6cdf774619b117ed4e1093701d30ac9b9 (origin/main, origin/HEAD, main)
Author: 666Daredevil666 <142442789+666Daredevil666@users.noreply.github.com>
Date:   Mon Sep 18 16:17:11 2023 +0300

    fix issue with rectangle

commit fdf9c176a8ba86f73aa9f35d4a994deb3b2e3028
Author: 666Daredevil666 <142442789+666Daredevil666@users.noreply.github.com>
Date:   Mon Sep 18 16:14:34 2023 +0300

    feat: add triangle

commit b1d38c534638dc1fdf02b37dd1c2d6cf55a555ef
Author: 666Daredevil666 <142442789+666Daredevil666@users.noreply.github.com>
Date:   Mon Sep 18 16:10:41 2023 +0300

    feat: add triangle

commit 834b7d83003bf36ea2ec2b879ceba6cee8025e3f (HEAD -> tests_408300)
Author: 666daredevil666 <bondarev.alex00555@gmail.com>
Date:   Thu Nov 16 13:03:17 2023 +0300

    add files and fix issues

##  Результаты тестирования
### Метрики
||            |
|:----:|:----------:|
| Запущено | 32 тестов  |
| Пройдено | 15 тестов  |
| Провалено | 17 тестов  |
| Общее время | 0.002 сек. |

### Отчет о дефектах
|           Модуль           | Пройдено | Провалено |                                          Дефекты                                           |
|:--------------------------:|:--------:|:---------:|:------------------------------------------------------------------------------------------:|
|     CircleTestCaseArea     |    2     |     2     | Неправильная работа программы при неккоректных входных данных и при больших входных данных |
|  CircleTestCasePerimeter   |    3     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |
| RectangleTestCasePerimeter |    4     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |
| RectangleTestCasePerimeter |    3     |     2     |          Неправильная работа программы при неккоректных входных данных и при нулевой стороне          |
|     SquareTestCaseArea     |    3     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |
|  SquareTestCasePerimeter   |    3     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |
|    TriangleTestCaseArea    |    3     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |
| TriangleTestCasePerimeter  |    3     |     1     |                     Неправильная работа программы при неккоректных входных данных                     |

    
