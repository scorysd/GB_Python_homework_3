# Задайте список из нескольких чисел. Напишите программу, которая найдёт
#  сумму элементов списка, стоящих на нечётной позиции.
numbers = list(input('Введите числа через пробел:').split())
index = 1
result = 0
print(numbers)
new_numbers = []
while index in range(len(numbers)):
    result = result + int(numbers[index])
    new_numbers.append(numbers[index])
    index += 2
print(f'На нечетных позициях стоят числа {new_numbers} их сумма равна: {result}')
