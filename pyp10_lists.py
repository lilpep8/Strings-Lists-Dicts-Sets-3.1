# Задача 1: Удаление дубликатов
def remove_duplicates(lst: list) -> list:
    without_duplicates_lst = []
    for i in lst:
        if i not in without_duplicates_lst:
            without_duplicates_lst.append(i)
    return without_duplicates_lst

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]


# Задача 2: Генерация списка квадратов
def generate_squares(n: int) -> list:
    return [x**2 for x in range(n+1) if x != 0]

print(generate_squares(5))


# Задача 3: Объединение двух списков
def merge_lists(list1: list, list2: list) -> list:
    list1.extend(list2)
    return list(set(list1))

print(merge_lists([1, 2, 3], [3, 4, 5]))


# Задача 4: Проверка на отсортированность
def is_sorted(lst: list) -> bool:
    return True if sorted(lst) == lst else False

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False


# Задача 5: Слияние списков
def merge_lists(list1: list, list2: list):
    return [x + y for x, y in zip(list1, list2)]

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]
