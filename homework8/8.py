import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_user_choice(ticket):
    """Получает выбор пользователя."""
    user_numbers = []
    for i, row in enumerate(ticket):
        while True:
            try:
                choice = int(input(f"Выберите число из строки {i+1} ({', '.join(map(str, row))}): "))
                if choice in row:
                    user_numbers.append(choice)
                    break
                else:
                    print("Число должно быть из этой строки.")
            except ValueError:
                print("Некорректный ввод. Введите число.")
    return user_numbers


def get_computer_choice(ticket):
    """Генерирует случайный выбор компьютера."""
    computer_numbers = [random.choice(row) for row in ticket]
    return computer_numbers

def calculate_statistics(user_numbers, computer_numbers):
    """Вычисляет статистику совпадений."""
    matches = 0
    for num in user_numbers:
        if num in computer_numbers:
            matches += 1
    return matches

user_numbers = get_user_choice(ticket)
computer_numbers = get_computer_choice(ticket)
matches = calculate_statistics(user_numbers, computer_numbers)

print("\nВаш выбор:", user_numbers)
print("Выбор компьютера:", computer_numbers)
print(f"Количество совпадений: {matches}")

