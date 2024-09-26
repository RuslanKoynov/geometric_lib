# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Functions 
## Circle
`area` function takes value r and returns it's square value multiplied on pi
```python
def area(r):
    return math.pi * r * r
```

`perimeter` function takes value r and multiplies it on 2 and pi
```python
def perimeter(r):
    return 2 * math.pi * r
```

## Rectangle
`area` function takes values a and b and returns result of their multiplication
```python
def area(a, b):
    return a * b
```

`perimeter` function takes values a and b and returns result of their multiplication
```python
def perimeter(a, b):
    return a * b
```

## Square
`area` function takes value a and returns it's square value
```python
def area(a):
    return a * a
```
`perimeter` function takes value a and returns it's value multiplied by 4
```python
def perimeter(a):
    return 4 * a
```

## Triangle
`area` function takes values of a and h and returns result of their mupltiplication divided by 2
```python
def perimeter(a, h):
    return a * h / 2
```
`perimeter` function takes values a, b, c and returns their sum
```python
def perimeter(a, b, c):
    return a + b + c
```

## Tests
`circle_tests` tests circle function for correct work and raising type and value errors for incorrect input data
```python
class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), pi*3**2)
        self.assertEqual(area(1), pi)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2.5), pi*2.5**2)
    def test_values(self):
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, area, 2+3j)
        self.assertRaises(TypeError, area, 'four')
        self.assertRaises(TypeError, area, [10, 31])
        self.assertRaises(TypeError, area, [6])
        self.assertRaises(TypeError, area, False)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 2*pi*3)
        self.assertEqual(perimeter(1), 2*pi)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(2.5), 2*pi*2.5)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 2+3j)
        self.assertRaises(TypeError, perimeter, 'four')
        self.assertRaises(TypeError, perimeter, [10, 31])
        self.assertRaises(TypeError, perimeter, [6])
        self.assertRaises(TypeError, perimeter, False)
```

`rectangle_tests` tests rectangle function for correct work and raising type and value errors for incorrect input data
```python
class RecrangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 2), 2*2)
        self.assertEqual(area(3, 1.5), 3*(1.5))
        self.assertEqual(area(3,5), 3*5)
        self.assertEqual(area(5,3), 5*3)
        self.assertEqual(area(2.3, 4.6), (2.3)*(4.6))
    def test_values(self):
        self.assertRaises(ValueError, area, 1, 0)
        self.assertRaises(ValueError, area, -7, 2)
        self.assertRaises(ValueError, area, -8, -9)
    def test_types(self):
        self.assertRaises(TypeError, area, 3+4j, 1+3j)
        self.assertRaises(TypeError, area, 'two', 'four')
        self.assertRaises(TypeError, area, [5], [4])
        self.assertRaises(TypeError, area, {3,5}, {4,7})

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 2), 2*2 + 2*2)
        self.assertEqual(perimeter(3, 1.5), 2*3 + 2*(1.5))
        self.assertEqual(perimeter(3,5), 2*3 + 2*5)
        self.assertEqual(perimeter(5,3), 2*5 + 2*3)
        self.assertEqual(perimeter(2.3, 4.6), 2*(2.3) + 2*(4.6))
    def test_values(self):
        self.assertRaises(ValueError, perimeter, 1, 0)
        self.assertRaises(ValueError, perimeter, -7, 2)
        self.assertRaises(ValueError, perimeter, -8, -9)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 3+4j, 1+3j)
        self.assertRaises(TypeError, perimeter, 'two', 'four')
        self.assertRaises(TypeError, perimeter, [5], [4])
        self.assertRaises(TypeError, perimeter, {3,5}, {4,7})
```

`square_tests` tests square function for correct work and raising type and value errors for incorrect input data
```python
class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 3*3)
        self.assertEqual(area(1), 1*1)
        self.assertEqual(area(2.5), (2.5)*(2.5))
    def test_values(self):
        self.assertRaises(ValueError, area, 0)
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, area, 2+3j)
        self.assertRaises(TypeError, area, 'four')
        self.assertRaises(TypeError, area, [6])
        self.assertRaises(TypeError, area, False)
        self.assertRaises(TypeError, area, [10, 31])

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 4*3)
        self.assertEqual(perimeter(1), 4*1)
        self.assertEqual(perimeter(2.5), 4*(2.5))
    def test_values(self):
        self.assertRaises(ValueError, perimeter, 0)
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 2+3j)
        self.assertRaises(TypeError, perimeter, 'four')
        self.assertRaises(TypeError, perimeter, [6])
        self.assertRaises(TypeError, perimeter, False)
        self.assertRaises(TypeError, perimeter, [10, 31])
```

`triangle_tests` tests triangle function for correct work and raising type and value errors for incorrect input data
```python
class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 5), 3*5/2)
        self.assertEqual(area(5, 3), 5*3/2)
        self.assertEqual(area(2.3, 4.6), (2.3)*(4.6))
        self.assertEqual(area(3, 1.5), 3*(1.5)/2)
    def test_values(self):
        self.assertRaises(ValueError, area, 1, 0)
        self.assertRaises(ValueError, area, -7, 2)
        self.assertRaises(ValueError, area, -8, -9)
    def test_types(self):
        self.assertRaises(TypeError, area, 3+4j, 1+3j)
        self.assertRaises(TypeError, area, 'two', 'four')
        self.assertRaises(TypeError, area, [5], [4])
        self.assertRaises(TypeError, area, {3,5}, {4,7})

    def test_perimeter(self):
        self.assertEqual(perimeter(2,3,4), 2+3+4)
        self.assertEqual(perimeter(2.6, 3.2, 8), 2.6 + 3.2 + 8)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -6, 3, 5)
        self.assertRaises(ValueError, perimeter, -2, -3, -6)
        self.assertRaises(ValueError, perimeter, 0, 3, 7)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'two', 3, 'one')
        self.assertRaises(TypeError, perimeter, [2], 3+6j, 11)
        self.assertRaises(TypeError, perimeter, 2, {3}, 9)
```

# Commits
| Author | Hash | Date | Commentary |
| --- | --- | --- | --- |
| Denis Gapilov <124xyz@mail.ru> | 0beb396ab3a48d905fcf4b4a617d8bbf32055eb6 | Wed Nov 15 18:16:37 2023 +0300 | test: triangle_tests fixed |
| Denis Gapilov <124xyz@mail.ru> | 97dd6ae21bdc3da77687ba75478a5fa598934f85 | Wed Nov 15 18:15:04 2023 +0300 | test: triangle_tests fixed |
| Denis Gapilov <124xyz@mail.ru> | ccd80c45bf16a57d042aae80073c4f9deef446c8 | Wed Oct 4 00:07:45 2023 +0300 | test: added tests for circle, rectangle, square, triangle |
| Denis Gapilov <124xyz@mail.ru> | 960b238c26f7de9fc50eb8a7f4bed9c80dd43d4a | Sun Sep 17 02:32:40 2023 +0300 | fix: perimeter calculation in rectangle.py |
| Denis Gapilov <124xyz@mail.ru> | 39fb6ff8e1adbee09cb8b57c14bc0be298d67d5e | Sun Sep 17 02:21:05 2023 +0300 | feat: created file rectangle.py |
| smartiqa <info@smartiqa.ru> | d078c8d9ee6155f3cb0e577d28d337b791de28e2 | Thu Mar 4 14:55:29 2021 +0300 | L-03: Docs added |
| smartiqa <info@smartiqa.ru> | 8ba9aeb3cea847b63a91ac378a2a6db758682460 | Thu Mar 4 14:54:08 2021 +0300 | L-03: Circle and square added |


# Tests
| Name | Tests Runned | Tests Failed | Success | Run Time |
| --- | --- | --- | --- | --- |
| circle_tests | 4 |  2 | 50% | 0.002 |
| rectangle_tests | 4 |  2 | 50% | 0.001 |
| square_tests | 4 |  2 | 50% | 0.001 |
| triangle_tests | 4 |  2 | 50% | 0.001 |

