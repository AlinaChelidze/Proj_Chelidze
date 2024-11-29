"""Составить программу, в которой функция генерирует четырехзначное
число и определяет, есть ли в числе одинаковые цифры"""
import random

def generate_and_check():
    """
    Генерирует четырехзначное число и
    проверяет на наличие одинаковых цифр.
    """

    num_str = ''.join(str(random.randint(0, 9)) for _ in range(4))
    num_set = set(num_str)

    if len(num_set) == 4:
        print(f"Сгенерированное число: {num_str}. Одинаковых цифр нет.")
    else:
        print(f"Сгенерированное число: {num_str}. Есть одинаковые цифры.")

generate_and_check()
