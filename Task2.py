# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from types import NoneType


x = NoneType
y = NoneType
z = NoneType

for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            if not(x or y or z) == (not(x) and not(y) and not(z)):
                print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ИСТИННО при X = {x}, Y = {y}, Z = {z}")
            else:
                print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ЛОЖНО при X = {x}, Y = {y}, Z = {z}")