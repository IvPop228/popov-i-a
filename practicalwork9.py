# -*- coding: utf-8 -*-

"""
Вариант 8

Задание 1:
Разделить элементы k-й строки на диагональный элемент
этой строки.

Задание 2:
Получить транспонированную матрицу.
"""

# Задание 1

n = int(input("Введите порядок матрицы: "))

A = []

for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = int(row[j])
    A.append(row)

k = int(input("Введите номер строки k: "))

d = A[k - 1][k - 1]

for j in range(n):
    A[k - 1][j] = A[k - 1][j] / d

print("Полученная матрица:")

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

# Задание 2

n = int(input("Введите порядок матрицы: "))

A = []

for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = int(row[j])
    A.append(row)

B = []

for i in range(n):
    B.append([0] * n)

for i in range(n):
    for j in range(n):
        B[j][i] = A[i][j]

print("Транспонированная матрица:")

for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()