# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
    # - x=34; y=-30 -> 4
    # - x=2; y=4-> 1
    # - x=-34; y=-30 -> 3

coord_x = float(input("Введите значение координаты X => "))
coord_y = float(input("Введите значение координаты Y => "))

if coord_x == 0 and coord_y == 0:
    print("Введите X ≠ 0 или Y ≠ 0!!!")
elif coord_x != 0 and coord_y == 0:
    print("Точка лежит на оси X")
elif coord_x == 0 and coord_y != 0:
    print("Точка лежит на оси Y")
elif coord_x > 0 and coord_y > 0:
    print("Точка находится в четверти 1")
elif coord_x < 0 and coord_y > 0:
    print("Точка находится в четверти 2")
elif coord_x < 0 and coord_y < 0:
    print("Точка находится в четверти 3")
else:
    print("Точка находится в четверти 4")