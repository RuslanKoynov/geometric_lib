- # [Общее описание решения](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#общее-описание-решения)

  ## [Содержит функции площади и периметра для 4 фигур](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#содержит-функции-площади-и-периметра-для-4-фигур)

  - Circle
  - Rectangle
  - Square
  - Triangle

  ### [Circle:](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#circle)

  - `def area` Получает радиус круга и возвращает его площадь
  - `def perimeter` Получает радиус круга и возвращает его периметр

  ### [Rectangle:](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#rectangle)

  - `def area` Получает длину двух сторон и возвращает площадь прямоугольника
  - `def perimeter` Получает длину двух сторон и возвращает периметр прямоугольника

  ### [Square:](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#square)

  - `def area` Получает длину стороны и возвращает площадь квадрата
  - `def area` Получает длину стороны и возвращает периметр квадрата

  ### [Triangle:](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#triangle)

  - `def area` Получает длину стороны и высоту треугольника и возвращает его площадь
  - `def perimeter` Получает длину трех сторон треугольника и возвращает его периметр

  # [Описание каждой функции с примерами вызова](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#описание-каждой-функции-с-примерами-вызова)

  ### [Функция площади круга](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-площади-круга)

  ```
  def area(r):
      return math.pi * r * r
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры)

  r - аргумент функции, который представляет собой радиус круга

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение)

  Функция возвращает площадь круга

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции)

  ```
  10
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции)

  ```
  314.1592
  ```

  

  ### [Функция периметра круга](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-периметра-круга)

  ```
  def perimeter(r):
      return 2 * math.pi * r
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-1)

  r - аргумент функции, который представляет собой радиус круга

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-1)

  Функция возвращает периметр круга

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-1)

  ```
  10
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-1)

  ```
  62.8318
  ```

  

  ### [Функция площади прямоугольника](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-площади-прямоугольника)

  ```
  def area(a, b):
      return a * b
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-2)

  a, b - аргументы функции, который представляет собой стороны прямоугольника

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-2)

  Функция возвращает площадь прямоугольника

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-2)

  ```
  10 20
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-2)

  ```
  200
  ```

  

  ### [Функция периметра прямоугольника](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-периметра-прямоугольника)

  ```
  def perimeter(a, b):
      return 2*(a + b)
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-3)

  a, b - аргументы функции, который представляет собой стороны прямоугольника

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-3)

  Функция возвращает периметр прямоугольника

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-3)

  ```
  10 20
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-3)

  ```
  60
  ```

  

  ### [Функция площади квадрата](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-площади-квадрата)

  ```
  def area(a):
      return a * a
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-4)

  a - аргументы функции, который представляет собой сторону прямоугольника

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-4)

  Функция возвращает площадь квадрата

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-4)

  ```
  10
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-4)

  ```
  100
  ```

  

  ### [Функция периметра квадрата](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-периметра-квадрата)

  ```
  def perimeter(a):
      return 4 * a
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-5)

  a - аргументы функции, который представляет собой сторону квадрата

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-5)

  Функция возвращает периметр квадрата

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-5)

  ```
  10
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-5)

  ```
  40
  ```

  

  ### [Функция площади треугольника](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-площади-треугольника)

  ```
  def area(a, h):
      return a * h / 2 
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-6)

  - a - аргумент функции, который представляет собой сторону треугольника
  - h - аргумент функции, который представляет собой высоту, проведённую к стороне a

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-6)

  Функция возвращает площадь треугольника

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-6)

  ```
  10 5
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-6)

  ```
  25
  ```

  

  ### [Функция периметра треугольника](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#функция-периметра-треугольника)

  ```
  def perimeter(a, b, c):
      return a + b + c
  ```

  

  ##### [Параметры](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#параметры-7)

  a , b, c- аргументы функции, который представляющие собой стороны треугольника

  ##### [Возвращаемое значение](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#возвращаемое-значение-7)

  Функция возвращает периметр треугольника

  ##### [Пример вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#пример-вызова-функции-7)

  ```
  10 15 20
  ```

  

  ##### [Результат вызова функции](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#результат-вызова-функции-7)

  ```
  45
  ```

  

  # [История изменения проекта с хешами коммитов](https://github.com/juyex/geometric_lib/blob/documentation_368743/docs/documentation.md#история-изменения-проекта-с-хешами-коммитов)

  - `5a733ff` fix: added documentation
  - `daa6536` fix: added documentation
  - `c25a232` fix: added documentation
  - `f5f5a5e` fix: added documentation
  - `695cba6` feat: add python file triangle fix: rectangle perimeter
  - `2361cca` feat: add python file of rectangle
  - `d078c8d` L-03: Docs added
  - `8ba9aeb` L-03: Circle and square added

