"""
Вариант 27
2. Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых
сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму.
"""
def find_K(N):

  if N <= 1:
      return "N должно быть больше 1"

  K = 1
  sum = 1
  while sum < N:
    K += 1
    sum += K
  return K, sum


N = 10
K, sum1 = find_K(N)
print(f"Наименьшее K для N = {N}: {K}, сумма: {sum1}")