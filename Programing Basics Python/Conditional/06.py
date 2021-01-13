import math

figure_type = input()

if figure_type == "square":
    first_side = float(input())
    print(f'{first_side * first_side:.3f}')

elif figure_type == "rectangle":
    first_side = float(input())
    second_side = float(input())
    print(f'{first_side * second_side:.3f}')

elif figure_type == "circle":
    radius = float(input())
    print(f'{math.pi * (radius * radius) :.3f}')

elif figure_type == "triangle":
    base = float(input())
    base_height = float(input())
    print(f'{(base_height * base) / 2 :.3f}')
