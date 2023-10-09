import math
length = float(input("Введите длину: "))
width = float(input("Введите ширину: "))
radius = float(input("Введите радиус: "))
base = float(input("Введите основание: "))
height = float(input("Введите высоту: "))

rectangle_area = length * width
print(f"Площадь прямоугольника: {rectangle_area}")
triangle_area = (base * height) / 2
print(f"Площадь прямоугольного треугольника: {triangle_area}")
square_area = length ** 2
print(f"Площадь квадрата: {square_area}")
circle_area = math.pi * radius ** 2
print(f"Площадь круга: {circle_area}")
depth = float(input("Введите глубину: "))
rectangular_prism_volume = length * width * depth
print(f"Объем прямоугольного параллелепипеда: {rectangular_prism_volume}")
cube_volume = length ** 3
print(f"Объем куба: {cube_volume}")
sphere_volume = (4 / 3) * math.pi * radius ** 3
print(f"Объем шара: {sphere_volume}")
cone_volume = (1 / 3) * math.pi * radius ** 2 * height
print(f"Объем конуса: {cone_volume}")