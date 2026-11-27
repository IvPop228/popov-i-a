# -*- coding: utf-8 -*-

"""
Вариант 8

Задание 1:
Разделить элементы k-й строки на диагональный элемент,
расположенный в этой строке.

Задание 2:
Получить транспонированную матрицу.
"""

file = open("Попов_Иван_Андреевич_У-263_vvod.txt", "r")

data = file.read().split()

file.close()

# Задание 1

n = int(data[0])

A = []
p = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(data[p]))
        p = p + 1
    A.append(row)

k = int(data[p])
p = p + 1

d = A[k - 1][k - 1]

for j in range(n):
    A[k - 1][j] = A[k - 1][j] / d

# Задание 2

m = int(data[p])
p = p + 1

B = []

for i in range(m):
    row = []
    for j in range(m):
        row.append(int(data[p]))
        p = p + 1
    B.append(row)

C = []

for i in range(m):
    C.append([0] * m)

for i in range(m):
    for j in range(m):
        C[j][i] = B[i][j]

# Запись результатов в файл

file = open("Попов_Иван_Андреевич_У-263_vivod.txt", "w", encoding="utf-8")

file.write("Задание 1:\n")

for i in range(n):
    for j in range(n):
        file.write(str(A[i][j]) + " ")
    file.write("\n")

file.write("\nЗадание 2:\n")

for i in range(m):
    for j in range(m):
        file.write(str(C[i][j]) + " ")
    file.write("\n")

file.close()