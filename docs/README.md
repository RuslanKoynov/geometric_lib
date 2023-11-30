 # About the project:

 *__This project is a set of modules for calculating areas and perimeters of figures such as circle, rectangle, square and triangle. All of them are written in Python language.__*

---
 ## Math formulas 

 ### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

 ### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

---

 ## Description of functions

 ### Circle's functions

 ##### **_area(*r*)_**

_- Calculates the area of a circle based on a given radius r._

 ***Example call:***
 ```python
  import circle
  print(circle.area(6))  
 ```  
***Example output***
```python
 113.09733552923255
```
 ##### **_perimeter(*r*)_** 

_- Calculates the perimeter of a circle based on a given radius r._

***Example call:*** 
```python
 import circle
 print(circle.perimeter(6))  
```  
 ***Example output:***
```python
 37.69911184307752
```

---

 ### Rectangle's functions 

 ##### **_area(a,b)_**

_- Calculates the area of a rectangle by given sides a and b._

***Example call:***
```python
 import rectangle
 print(rectangle.area(3, 7))  
```  
***Example output:***
```python
 21  
```
 ##### **_perimeter(a,b)_** 

_- Calculates the perimeter of a rectangle by given sides a and b._

*Example call:*
```python
 import rectangle
 print(rectangle.perimeter(3, 7))  
```  
*Example output:*
```python
 20  
```
--- 
 ### Square's functions

 ##### **_area(a)_**

_- Calculates the area of a square from a given side a._

***Example call:***
```python
 import square
 print(square.area(5))  
```  
***Example output:***
```python
 25  
```

 ##### **_perimeter(a)_** 

_- Calculates the perimeter of a square from a given side a._

***Example call:***
```python
 import square
 print(square.perimeter(5))  
```  
 ***Example output:***
```python
 20  
```
 
 ---
 
 ### Triangle's functions
 
 ##### **_area(a,h)_**

_- Calculates the area of a triangle from the given base a and height h._

 ***Example call:***
```python
 import triangle
 print(triangle.area(7, 8))  
```  
***Example output:***
```python
 28  
```
 ##### **_perimeter(a,b,c)_** 

_- Calculates the perimeter of a triangle from given sides a, b and c._

***Example call:***
```python
 import triangle
 print(triangle.perimeter(3, 6, 8))  
```  

***Example output:***
```python
 17  
```
 
---

## Autotests succes:
~~~
- 39 - all tests;
- 0 - tests with errors;
- 39 - correct tests(100%);
~~~

---
 
 # History of project changes

| **Hash**                                     | **Author**                       | **Comments**                                                       |
|:------------------------------------------:|:------------------------------:|:----------------------------------------------------------------:|
| 8ba9aeb3cea847b63a91ac378a2a6db758682460 | smartiqa <info@smartiqa.ru> | L - 03 :  Circle   and   square   added                        |
| d078c8d9ee6155f3cb0e577d28d337b791de28e2 | smartiqa <info@smartiqa.ru> | L - 03 :  Docs   added                                         |
| ed967f4431e664123c976277df4473b93bea2b53 | Floym7 <floym7@mail.ru>  | new   file   added                                             |
| 0772a7cefea25ffc72ac4460463430c13a630b14 | FFloym7 <floym7@mail.ru>  | the   error   has   been   fixed                               |
| 6f71a6d31af3a5bf77f90db3852fc2536cc24085 | Floym7 <floym7@mail.ru>  | docs :  added   comments   for   each   of   the   functions   |
| aa37ad0fd8a3872a71117a81df34337760fbbece | Floym7 <floym7@mail.ru>  | refactor: calculation logic with integrated exception handling |
| ce43951ca672907816a1857c4f8b16d6090fe86a | Floym7 <floym7@mail.ru>  | test: added unit tests        
| 421878709135e1d0cf4a9df3cdd1e07e7df772cc | Floym7 <floym7@mail.ru>  | triangle: improved exception handling  |

- ___Created by Shumeiko Aleksandr___
 