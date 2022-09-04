# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
    # - 6 -> да
    # - 7 -> да
    # - 1 -> нет

day_number = int(input("Введите номер дня недели: "))

if (day_number < 1) or (day_number > 7):
    print("Такого дня недели нет!")
elif 0 < day_number < 6:
    print("Будний день(")
else:
    print("Ура, выходной!!!")