# # Задача 1: Анаграмма
# def is_anagram(s1, s2):
#     return sorted(list(s1.lower())) == sorted(list(s2.lower()))
#
# print(is_anagram("Listen", "silent"))  # True
# print(is_anagram("hello", "World"))    # False


# # Задача 2: Палиндром
# def is_palindrome(s):
#     clean_s = "".join(char for char in s if char.isalpha())
#     return clean_s.lower() == clean_s.lower()[::-1]
#
# print(is_palindrome("racecar"))
# print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("hello"))

# Задача 3: Самое длинное слово
#
# def longest_word(s):
#     new_s = ''
#     for i in range(len(s)-1):
#         if s[i].isalpha() is True or s[i] == ' ':
#             new_s += s[i]
#     words = new_s.strip().split(' ')
#
#     print (max(words, key=len))
#
#
# longest_word("In the middle of a vast desert, an extraordinary adventure awaits")
# longest_word(',,,,')


# # Задача 4: Форматирование номера телефона
# def format_phone_number(digits):
#     if len(digits) == 10:
#         formated_digits = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
#         return formated_digits
# print(format_phone_number("1234567890"))

# Задача 5: Удаление дублирующих символов
# def remove_duplicates(s):
#     formatted_s = ''
#     for i in s:
#         if i not in formatted_s:
#             formatted_s += i
#     print(formatted_s)
#
# remove_duplicates("programming")

# задача 6: Проверка на уникальность символов
#
# def is_unique(s):
#     return True if len(s) == len(set(s)) else False
#
# print(is_unique("abcdef"))
# print(is_unique("hello"))