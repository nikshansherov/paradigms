# Императивный стиль

def sort_list_imperative(numbers):
    sw = True
    while sw:
        sw = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                sw = True
    return numbers
