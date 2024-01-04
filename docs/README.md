# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описание проекта

### В этом проекте реализованы различные математические формулы, а именно:
1. Формулы площади для круга, прямоугольника, квадрата и треугольника
2. Формулы периметра для круга, прямоугольника, квадрата и треугольника

## Описание работы circle.py
### 1. Описание функции area(`r`):
### Параметры
- `r` – радиус круга
### Результат работы функции
- Площадь круга с радиусом `r`
### Пример вызова функции
- area(`10.0`) → 314.1592653589793

### 2. Описание функции perimeter(`r`):
### Параметры
- `r` – радиус круга
### Результат работы функции
- Периметр круга с радиусом `r`
### Пример вызова функции
- perimeter(`11`) → 69.11503837897544

## Описание работы rectangle.py
### 1. Описание функции area(`a`, `b`):
### Параметры
- `a` – первая сторона прямоугольника
- `b` – вторая сторона прямоугольника
### Результат работы функции
- Площадь прямоугольника со сторонами `a` и `b`
### Пример вызова функции
- area(`4`, `9`) → 36
### 2. Описание функции perimeter(`a`, `b`):
### Параметры
- `a` – первая сторона прямоугольника
- `b` – вторая сторона прямоугольника
### Результат работы функции
- Периметр прямоугольника со сторонами `a` и `b`
### Пример вызова функции
- perimeter(`6`, `7`) → 30

## Описание работы square.py
### 1. Описание функции area(`a`):
### Параметры
- `a` – сторона квадрата
### Результат работы функции
- Площадь квадрата со стороной `a`
### Пример вызова функции
- area(`5`) → 25
### 2. Описание функции perimeter(`a`):
### Параметры
- `a` – первая сторона квадрата
### Результат работы функции
- Периметр квадрата со стороной `a`
### Пример вызова функции
- perimeter(`7`) → 28

## Описание работы triangle.py
### 1. Описание функции area(`a`, `h`):
### Параметры
- `a` – основание треугольника
- `h` – высота треугольника
### Результат работы функции
- Площадь треугольника с основанием `a` и высотой `h`
### Пример вызова функции
- area(`22`, `8`) → 88.0
### 2. Описание функции perimeter(`a`, `b`, `c`):
### Параметры
- `a` – первая сторона треугольника
- `b` – вторая сторона треугольника
- `c` – третья сторона треугольника
### Результат работы функции
- Периметр треугольника со сторонами `a`, `b` и `c`
### Пример вызова функции
- perimeter(`3`, `4`, `5`) → 12

# История версий
- v.0.0.1 – добавлены файлы rectangle.py и triangle.py
- v.0.0.2 – добавлена докуменация
- v.0.0.3 – добавлены unit-тесты

# История изменений проекта
commit 197930bd36563c6c9303ffc4b23f78fcc6074182 (HEAD -> main)
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Tue Nov 21 23:52:56 2023 +0300

    test: add unit tests for triangle.py

commit 09967ee286748638978221e6a192342d6bac9dd1
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Tue Nov 21 23:52:38 2023 +0300

    test: add unit tests for square.py

commit d42edbd6556c04c5884e330ef67d829b4daa3427
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Tue Nov 21 23:51:54 2023 +0300

    test: add unit tests for rectangle.py

commit 9710b8fc6ed41bf38fb79f65ddbb98933ae88c98
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Tue Nov 21 23:50:46 2023 +0300

    test: add unit tests for circle.py

commit eb2777b47135de64479bc389461b8bdf9293fc98 (HEAD -> laboratory)
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Sat Sep 30 23:43:59 2023 +0300

    docs: add documentation for the triangle.py file

commit b0cd8cbf7e83817fb98a14b35d51490b48f1b61d
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Sat Sep 30 23:43:36 2023 +0300

    docs: add documentation for the square.py file

commit 846f54b289c44b98dd9582a87cf8efe9ce5ed67a
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Sat Sep 30 23:42:18 2023 +0300

    docs: add documentation for the rectangle.py file

commit c9504cdd3ed916cb95936bc5ab82766eb41d1ea7
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Sat Sep 30 23:41:33 2023 +0300

    docs: add documentation for the circle.py file

commit 9e85430f51205743fb6c5342c106edd6aea32f94 (main)
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Mon Sep 25 22:03:32 2023 +0300

    Исправлена ошибка в вычислении периметра прямоугольника

commit 1733cb4bda07488b6dfa794f48f25b22cf3d3149
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Mon Sep 25 22:00:44 2023 +0300

    Добавлен файл с вычислениями для треугольника

commit 42890c9e921d3c16106fe39980025e62b0f9a8d4
Author: Georgiy Yanchenko <ihengeo@gmail.com>
Date:   Mon Sep 25 21:56:41 2023 +0300

    Добавлен новый файл с вычислениями для прямоугольника

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added