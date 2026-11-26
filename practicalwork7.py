# -*- coding: utf-8 -*-

"""
Вариант 8

Задание 1:
Найти сумму и произведение элементов списка.

Задание 2:
Заменить нулевые элементы массива
средним арифметическим всех элементов.
"""

# Задание 1

n = int(input("Введите количество элементов: "))
a = [int(input()) for i in range(n)]

s = 0
p = 1

for i in range(n):
    s = s + a[i]
    p = p * a[i]

print("Сумма:", s)
print("Произведение:", p)

# Задание 2

n = int(input("Введите количество элементов: "))
b = [float(input()) for i in range(n)]

s = 0

for i in range(n):
    s = s + b[i]

average = s / n

for i in range(n):
    if b[i] == 0:
        b[i] = average

print("Полученный массив:", b)



