# -*- coding: utf-8 -*-

"""
Задание 8:
Определить наибольшее количество подряд идущих
одинаковых элементов последовательности.
"""

a = int(input())
count = 0
max_count = 0
previous = 0

while a != 0:
    if a == previous:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

    previous = a
    a = int(input())

print(max_count)