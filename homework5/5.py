numbers = [1, 5, 2, 8, 3, 9, 4] 

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])
