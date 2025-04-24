# # Задача 1: Частотный анализ строки
# def char_frequency(s):
#
#     dct_s = {i: s.count(i) for i in s}
#     print(dct_s)
#
# char_frequency("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#

# # Задача 2: Слияние двух словарей
# def merge_dicts(d1, d2):
#     return {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
#
#
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# print(merge_dicts(d1, d2))# {"a": 1, "b": 5, "c": 4}


# Задача 3: Обратное преобразование словаря в два списка
# def dict_to_lists(my_dict):
#     k, v = [], []
#     for keys, values in my_dict.items():
#         k.append(keys)
#         v.append(values)
#     return (k,v)
#
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])
#

# # Задача 4: Группировка элементов по первому символу
#
# def group_by_first_letter(strings):
#     dct = {x[0]: [x] for x in (strings)}
#     for key,value in dct.items():
#         for j in strings:
#             if j not in value and j[0] == key:
#                 value.append(j)
#     return(dct)
#
# strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings)) # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}



# Задача 5: Извлечение подсловаря
# def extract_subdict(my_dict, keys):
#     z = {}
#     for i in keys:
#         for key, value in my_dict.items():
#             if i == key:
#                 z[key] = [value]
#
#     return z
#
#
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}
