"""
Вариант 27.
1. Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
"""

def sum_of_fractions(N):

  if N <= 1:
      return "N должно быть больше 1"

  sum = 0
  for i in range(1, N + 1):
    sum += 1 / i
  return sum

N = 3
sum1 = sum_of_fractions(N)
print(f"Сумма для N = {N}: {sum1}")