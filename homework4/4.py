numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число или 'end'.")

even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)

