from random import randint


def bin_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lst = list(set(randint(1, 30) for i in range(1, 20)))
lst.sort()
print(lst)

target = int(input('Введите искомый элемент: '))
result = bin_search(lst, target)

if result == -1:
    print('Элемент отсутствует в списке')
else:
    print(f'Индекс искомого элемента = {result}')
