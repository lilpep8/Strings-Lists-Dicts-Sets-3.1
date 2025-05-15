# Задача 1: Анаграмма
def is_anagram(s1: str, s2: str) -> bool:
    return sorted(list(s1.lower())) == sorted(list(s2.lower()))

print(is_anagram("Listen", "silent"))  # True
print(is_anagram("hello", "World"))    # False


# Задача 2: Палиндром
def is_palindrome(s: str) -> bool:
    clean_s = "".join(char for char in s if char.isalpha())
    return clean_s.lower() == clean_s.lower()[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("hello")) # False


# Задача 3: Самое длинное слово
def longest_word(s: str) -> str:
    clear_string = ''
    for i in range(len(s)):
        if s[i].isalpha() or s[i] == ' ':
            clear_string += s[i]

    words = clear_string.strip().split(' ')
    answer = (max(words, key=len))
    return answer

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits")) # "extraordinary”
print(longest_word(',,,,'))


# Задача 4: Форматирование номера телефона
def format_phone_number(digits: str) -> str :
    if len(digits) != 10 or not digits.isdigit():
        raise ValueError("Номер должен содержать ровно 10 цифр")
    formated_digits = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return formated_digits

print(format_phone_number("1234567890"))
print(format_phone_number("123456789"))
print(format_phone_number("adadada"))
print(format_phone_number(""))


# Задача 5: Удаление дублирующих символов
def remove_duplicates(s: str) -> str:
    formatted_s = ''
    for i in s:
        if i not in formatted_s:
            formatted_s += i
    return formatted_s

print(remove_duplicates("programming")) # "progamin”
print(remove_duplicates("1112233345")) # "12345”
print(remove_duplicates("")) # "”


# Задача 6: Проверка на уникальность символов
def is_unique(s: str) -> bool:
    return True if len(s) == len(set(s)) else False

print(is_unique("abcdef"))#  True
print(is_unique("hello"))#  False
