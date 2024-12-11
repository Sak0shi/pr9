numbers = [3, 1, 4, 1, 5, 9, 2, 6]

min_val = min(numbers)
max_val = max(numbers)

min_index = numbers.index(min_val)
max_index = numbers.index(max_val)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(numbers)
