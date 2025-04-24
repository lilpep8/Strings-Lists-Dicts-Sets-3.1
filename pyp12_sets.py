# # Задача 1: Уникальные элементы списка
#
# def get_unique_elements(lst):
#     return list(set(lst))
#
# print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]


# # Задача 2: Проверка списка на уникальность элементов
#
# def is_unique_list(lst):
#     return True if len(lst) == len(set(lst)) else False
#
# print(is_unique_list([1, 2, 3, 4]))  # True
# print(is_unique_list([1, 2, 2, 3]))  # False


# # Задача 3: Получение уникальных гласных из строки
#
# def get_unique_vowels(s):
#     s = [x for x in s if x in ["a", "e", "i", "o", "u"]]
#     return set(s)
# print(get_unique_vowels("Hello World"))  # {'e', 'o'}