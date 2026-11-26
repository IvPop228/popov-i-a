# -*- coding: utf-8 -*-

"""
Вариант 8

Задание 1:
Найти все натуральные числа, не превосходящие n,
которые делятся на каждую из своих цифр.
"""

n = int(input("Введите n: "))

for i in range(1, n + 1):
    a = i
    flag = True

    while a > 0 and flag:
        digit = a % 10

        if digit == 0 or i % digit != 0:
            flag = False

        a = a // 10

    if flag:
        print(i, end=" ")

"""
Задание 2:
Поменять местами первый и последний элементы массива.
"""

def zam(A):
    temp = A[0]
    A[0] = A[len(A) - 1]
    A[len(A) - 1] = temp

m = int(input("\nВведите длину массива: "))

A = []

for i in range(m):
    A.append(int(input("Введите элемент массива: ")))

print("Исходный массив:", A)

zam(A)

print("Полученный массив:", A)





