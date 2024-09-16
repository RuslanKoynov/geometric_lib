import circle
import rectangle
import square
import triangle


def manual_test_square_area():
    input_ = int(input("Введите длину стороны квадрата "))
    res = square.area(input_)
    print(res)


def manual_test_square_perimeter():
    input_ = int(input("Введите длину стороны квадрата "))
    res = square.perimeter(input_)
    print(res)


def manual_test_circle_area():
    input_ = int(input("Введите длину радиуса окружности "))
    res = circle.area(input_)
    print(res)


def manual_test_circle_perimeter():
    input_ = int(input("Введите длину радиуса окружности "))
    res = circle.perimeter(input_)
    print(res)


def manual_test_rectangle_area():
    input_ = list(map(int, (input("Введите длины стороны прямоугольника через пробел ").split(" "))))
    res = rectangle.area(input_[0], input_[1])
    print(res)


def manual_test_rectangle_perimeter():
    input_ = list(map(int, (input("Введите длины сторон прямоугольника через пробел ").split(" "))))
    res = rectangle.perimeter(input_[0], input_[1])
    print(res)


def manual_test_triangle_area():
    input_ = list(map(int, (input("Введите длину стороны треугольника и длину высоты, проведённой к этой стороне, "
                                  "через пробел ").split(" "))))
    res = triangle.area(input_[0], input_[1])
    print(res)


def manual_test_triangle_perimeter():
    input_ = list(map(int, (input("Введите длины сторон треугольника ").split(" "))))
    res = triangle.perimeter(input_[0], input_[1], input_[2])
    print(res)


while True:
    print("Выберите команду\n 1 - вычисление площади квадрата\n 2 - вычисление периметра квадрата\n 3 - вычисление "
          "площади круга\n 4 - вычисление длины окружности\n 5 - вычисление площади прямоугольника\n 6 - вычисление "
          "периметра прямоугольника\n 7 - вычисление площади треугольника\n 8 - вычисление периметра треугольника\n 9 "
          "- выход")
    res = int(input())

    if res == 1:
        manual_test_square_area()
    if res == 2:
        manual_test_square_perimeter()
    if res == 3:
        manual_test_circle_area()
    if res == 4:
        manual_test_circle_perimeter()
    if res == 5:
        manual_test_rectangle_area()
    if res == 6:
        manual_test_rectangle_perimeter()
    if res == 7:
        manual_test_triangle_area()
    if res == 8:
        manual_test_triangle_perimeter()
    if res == 9:
        break






