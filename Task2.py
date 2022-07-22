# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numbers = list(input('Введите числа через пробел:').split())
index = 0
result = 1
new_numbers = []
while index in range(len(numbers) // 2):
    result = int(numbers[index]) * int(numbers[-index - 1])
    new_numbers.append(result)
    index += 1
if len(numbers) % 2 != 0:
    new_numbers.append((int(numbers[len(numbers) % 2 + 1])) ** 2)
print(f'{numbers} --> {new_numbers}')