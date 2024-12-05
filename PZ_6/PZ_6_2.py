"""
Вариант 27
Дан целочисленный список A размера N. Переписать в новый целочисленный
список B все четные числа из исходного списка (в том же порядке) и вывести размер
полученного список B и его содержимое.
"""
import random

random_list = []
total_list = []

for i in range(random.randint(5, 20)):
    random_list.append(random.randint(1, 100))


for i in random_list:
    if i % 2 == 0:
        total_list.append(i)

print(f'Данный список: {random_list}\nСписок с чётными числами: {total_list}\nРазмер: {len(total_list)}')