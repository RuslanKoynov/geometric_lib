# Geometric Lib

- ***Вычисляет площадь и периметр геометрических фигур.***

## Поддерживает работу:

### 1) Circle.py
- `def area(r)` получает *радиус круга* и возвращает его площадь, рассчитанную по формуле **S = πR<sup>2</sup>**
    > import math \
     result = area(3) \
     print(result) \
  > \
  `28.274333882308138`
- `def perimeter(r)` получает *радиус круга* и возвращает его периметр, рассчитанный по формуле **P = 2πR**
    > import math \
     result = perimeter(3) \
     print(result) \
  > \
  `18.84955592153876`

### 2) Rectangle.py
- `def area(a, b)` получает *длину сторон прямоугольника* и возвращает его площадь, рассчитанную по формуле **S = a * b**
    > result = area(2, 3) \
     print(result) \
  > \
  `6`
- `def perimeter(a, b)` получает *длину сторон прямоугольника* и возвращает его периметр, рассчитанный по формуле **P = 2 * (a + b)**
    > result = perimeter(2, 3) \
     print(result) \
  > \
  `10`

### 3) Square.py
- `def area(a)` получает *длину стороны квадрата* и возвращает его площадь, рассчитанную по формуле **S = a<sup>2</sup>**
    > result = area(2) \
     print(result) \
  > \
  `4`
- `def perimeter(a)` получает *длину стороны квадрата* и возвращает его периметр, рассчитанный по формуле **P = 4 * a**
    > result = perimeter(2) \
     print(result) \
  > \
  `8`

### 4) Triangle.py
- `def area(a, h)` получает *длину основания треугольника* и *его высоту* и возвращает площадь, рассчитанную по формуле **S = a * (h / 2)**
    > result = area(5, 4) \
     print(result) \
  > \
  `10`
- `def perimeter(a, b, c)` получает *длину всех сторон треугольника* и возвращает его периметр, рассчитанный по формуле **P = a + b + c**
    > result = perimeter(1, 2, 3) \
     print(result) \
  > \
  `6`

## История изменений проекта:

- commit fa132ab (HEAD -> main)
Author: mhgffqwoer <a.yakshevich2005@gmail.com>
Date:   Wed Oct 4 21:45:20 2023 +0300

  >add documentation

- commit 4969630
Author: mhgffqwoer <a.yakshevich2005@gmail.com>
Date:   Sat Sep 16 12:45:45 2023 +0300

  >добавлен новый файл triangle.py и исправлена ошибка в файле rectangle.py

- commit e55b35e
Author: mhgffqwoer <a.yakshevich2005@gmail.com>
Date:   Sat Sep 16 12:41:33 2023 +0300

  >добавлен новый файл rectangle.py

- commit d078c8d
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

  >L-03: Docs added

- commit 8ba9aeb
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
  >L-03: Circle and square added