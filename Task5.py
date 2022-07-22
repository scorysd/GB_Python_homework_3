# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
fib_1 = 1
fib_2 = 1
amount = int(input('Введите число:'))
result = []
result.append(fib_1)
result.append(fib_2)
for i in range(2, amount):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    result.append(fib_2)
negafibo = [result[i] * -1 for i in  range(len(result))]
print(list(reversed(negafibo)) + result)