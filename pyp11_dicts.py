# Задача 1: Частотный анализ строки
def char_frequency(s: str) -> dict:
    s = s.lower()
    frequency = {}
    symbols = set(s)

    for i in symbols:
        frequency[i] = 0

    for i in s:
        if i in frequency.keys():
            frequency[i] += 1

    return frequency

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(char_frequency("llll"))  # {'l': 4}


# Задача 2: Слияние двух словарей
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    return {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))# {"a": 1, "b": 5, "c": 4}


# Задача 3: Обратное преобразование словаря в два списка
def dict_to_lists(my_dict: dict) -> tuple:
    return list(my_dict.keys()),list(my_dict.values())

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])


# Задача 4: Группировка элементов по первому символу
def group_by_first_letter(strings: list) -> dict:
    group = {}
    for word in strings:
        key = word[0]
        if key not in group:
            group[key] = []
        group[key].append(word)

    sorted_group = dict(sorted(group.items()))
    return sorted_group

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings)) # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}


# Задача 5: Извлечение подсловаря
def extract_subdict(my_dict: dict, keys: list) -> dict:
    subdict = {}
    for i in keys:
        for key, value in my_dict.items():
            if i == key:
                subdict[key] = [value]

    return subdict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}
