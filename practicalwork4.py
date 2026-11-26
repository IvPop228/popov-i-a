# -*- coding: utf-8 -*-

"""
Задание 8:
Вывести лесенку из n ступенек.
"""

n = int(input("Введите число: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()