def squares_between(a, b):
    """
    Создает список квадратов целых чисел между a и b.

    Args:
        a: Начальное число.
        b: Конечное число.

    Returns:
        Список квадратов целых чисел между a и b. 
        Возвращает пустой список, если a >= b.
    """
    if a >= b:
        return [] 

    squares = []
    for i in range(a + 1, b):
        squares.append(i*2)
    return squares

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = squares_between(a, b)
print("Список квадратов чисел между", a, "и", b, ":", result)

