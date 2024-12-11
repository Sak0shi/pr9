numbers = [1, 2, 3, 4, 5]

last_element = numbers[-1] # Сохраняем последний элемент

for i in range(len(numbers) - 1, 0, -1): # Итерация в обратном порядке
    numbers[i] = numbers[i - 1]

numbers[0] = last_element # Перемещаем последний элемент на первое место

print(numbers) # Вывод: [5, 1, 2, 3, 4]
