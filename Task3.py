# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
import math
amount = int(input('Введите количество элементов массива:'))
numbers = [random.randrange(1000) / 100 for i in range(amount)]
new_numbers = []
for e in numbers:
    new_numbers.append((round(100 * (e - math.floor(e)))))
print(f'Разница между максимальной ({max(new_numbers)/100}) и минимальной ({min(new_numbers) /100}) дробной частью чисел {numbers} равна: {(max(new_numbers) - min(new_numbers)) / 100}')