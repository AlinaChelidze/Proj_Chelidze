"""
Вapиант 27
Дан список А размера N. Найти минимальный элемент из его элементов с четными номерами: А2, А4, Аб, ... .
"""
import random

random_list = []

for i in range(random.randint(5, 20)):
    random_list.append(random.randint(0, 100))

def min(A):
    min = float('inf')
    for i in range (1, len(A), 2):
        if A[i] < min:
            min = A[i]
    return min

print(f'В списке:{random_list}\nМинимальное число среди елементов с чётными номерами {min(random_list)}')
