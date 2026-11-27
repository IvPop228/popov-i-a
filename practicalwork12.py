# -*- coding: utf-8 -*-

# Блок А, задание 2

def ostatok(a, b):
    if a < b:
        return a
    return ostatok(a - b, b)

a = int(input("Введите a: "))
b = int(input("Введите b: "))

print("Остаток:", ostatok(a, b))

# Блок Б, задание 2

def second_max(max1, max2):
    n = int(input("Введите число (0 для завершения): "))

    if n == 0:
        return max2

    if n > max1:
        return second_max(n, max1)
    elif n > max2:
        return second_max(max1, n)
    else:
        return second_max(max1, max2)

print("Второй максимум:", second_max(0, 0))