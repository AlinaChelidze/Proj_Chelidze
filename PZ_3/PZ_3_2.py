"""
Вариант 27
Дан номер месяца — целое число в диапазоне 1-12
(1 — январь, 2 — февраль и т. д.).
Вывести название соответствующего времени года
(«зима», «весна», «лето», «осень»).
"""
def typecheck(x, type_):
  while type(x) != type_:
    try:
      return type_(x)
    except ValueError:
      x = input('Неправильный ввод числа!\nПовторите ввод: ')

month = input("Введите номер месяца (1-12): ")
month = typecheck(month, int)

if month in (12, 1, 2):
  season = "зима"
elif month in (3, 4, 5):
  season = "весна"
elif month in (6, 7, 8):
  season = "лето"
elif month in (9, 10, 11):
  season = "осень"
else:
  season = "Некорректный номер месяца"

print(f"Время года: {season}")
